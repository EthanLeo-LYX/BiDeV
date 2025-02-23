import os
import re
import json
import tqdm
import random
import argparse
import threading
from queue import Queue
from rouge import Rouge

from utils.prompt_utils import *
from utils.api_utils import get_api_request
from utils.data_utils import load_data, get_mini_batch
from utils.qa_utils import T5_Question_Answering
from utils.retriever_utils import PyseriniRetriever

uncertain_info_query_template = uncertain_info_query
claim_rewrite_template = claim_rewrite
decompose_template = verify_decomp
evidence_filter_template = evidence_filter


def retrieve_evidence(query, retrieve_model, top_k=10, max_length=3000):
    hits = retrieve_model.retrieve(query, top_k)
    evidence = '\n'.join([hit['text'].strip() for hit in hits])
    # cut overlong evidence
    if len(evidence.split()) > max_length:
        print('evidence is too long, cut it to max_evidence_length')
        evidence = ' '.join(evidence.split()[:max_length])

    # save retrieval results (can comment out if not needed)
    retrieved_results = []
    for hit in hits:
        retrieved_results.append({'id': hit['doc_id'], 'score': hit['score'], 'query': query})

    return evidence, retrieved_results


def extract_evidence(response, evidence):
    response = response.split('\n')[1:]
    evidence = evidence.split('\n')
    if len(response) != len(evidence):
        return '\n'.join(evidence)
    output = []
    for i in range(len(response)):
        if 'irrelevant' in response[i]:
            continue
        else:
            output.append(evidence[i])
    if len(output) <= 1:
        output = []
        output.extend(evidence)
    return '\n'.join(output)


def filter(claims, evidences):
    messages = [message_format(evidence_filter_template, {'claim': claim, 'evidence': e}) for claim, e in zip(claims, evidences)]
    responses = get_api_request(messages, max_tokens=256)
    filtered_evidences = [extract_evidence(res, e) for res, e in zip(responses, evidences)]
    for i in range(len(filtered_evidences)):
        if filtered_evidences[i] == '':
            filtered_evidences[i] = evidences[i]
    return filtered_evidences


def extract_question(response):
    pattern = re.compile(r'<<<.+?>>>')
    question = pattern.findall(response)
    if len(question) <= 1:
        return 'Easy Claim', None
    else:
        return 'Complex Claim', question[1].replace('<<<', '').replace('>>>', '')


def perceptor(claim, previous_questions):
    if len(previous_questions) > 0:
        claim = claim + '\n' + 'Do not ask the following questions: \n' + '\n'.join(previous_questions)
    message = message_format(uncertain_info_query_template, {'claim': claim,})
    response = get_api_request([message], max_tokens=512)[0]
    decision, question = extract_question(response)
    return decision, question


def valid_question(question):
    if question is None:
        return None
    if 'What' in question or 'Which' in question or 'Who' in question \
            or 'When' in question or 'How' in question or 'Where' in question:
        return question
    else:
        return None


def extract_answer(response):
    pattern = re.compile(r'<<<.+?>>>')
    answer = pattern.findall(response)
    if len(answer) == 0:
        return None
    else:
        return answer[0].replace('<<<', '').replace('>>>', '')


def querier(question, evidence, qa_model, retrieve_model):
    if evidence is None:
        evidence = retrieve_evidence(question, retrieve_model)[0]
        evidence = filter([question], [evidence])[0]
    answer = qa_model.answer_question_directly(question, evidence)['answer_text']
    return answer


def extract_rewrite_claim(response):
    pattern = re.compile(r'<<<.+?>>>')
    rewrite_claim = pattern.findall(response)
    if len(rewrite_claim) == 0:
        return None
    else:
        return rewrite_claim[0].replace('<<<', '').replace('>>>', '')


def rewriter(claim, question, answer):
    message = message_format(claim_rewrite_template, {'claim': claim, 'question': question, 'answer': answer})
    response = get_api_request([message], max_tokens=512)[0]
    # print('Rewrite Response:')
    # print(response)
    rewrite_claim = extract_rewrite_claim(response)
    if rewrite_claim is None:
        return claim
    if Rouge().get_scores([claim], [rewrite_claim], avg=True)['rouge-l']['r'] > 0.5:
        return rewrite_claim
    else:
        return claim


def perceive_then_rewrite(claim, evidence, qa_model, retrieve_model, max_iter=3):
    processed_claim = claim
    certain_enough = False
    # print('###########################################################################')
    # print('Initial Claim:')
    # print(claim)
    previous_questions = []
    question_answers = []
    history_claims = []
    while max_iter > 0:
        # print('***************************************************************************')
        # print('Iter ', 3 - max_iter + 1)
        max_iter -= 1
        decision, question = perceptor(processed_claim, previous_questions)
        question = valid_question(question)
        # print('Question:')
        # print(question)
        if 'Easy Claim' in decision:
            if not certain_enough:
                certain_enough = True
                continue
            else:
                break
        else:
            if question is None:
                continue
            else:
                previous_questions.append(question)
        answer = querier(question, evidence, qa_model, retrieve_model)
        # print('Answer:')
        # print(answer)
        if answer is None:
            continue
        processed_claim = rewriter(processed_claim, question, answer)
        question_answers.append(answer)
        history_claims.append(processed_claim)
        # print('Rewrite Claim:')
        # print(processed_claim)
    return processed_claim, history_claims, previous_questions, question_answers


def extract_sub_claims(response):
    lines = response.split('\n')[1:]
    output = [line for line in lines if line != '']
    return output


def get_sub_claims(claim):
    message = message_format(decompose_template, {'claim': claim})
    response = get_api_request([message], max_tokens=512)[0]
    sub_claims = extract_sub_claims(response)
    return sub_claims


def extract_verify_result(response):
    if 'True' in response:
        return True
    if 'False' in response:
        return False
    return response


def map_direct_answer_to_label(predict):
    predict = predict.lower().strip()
    label_map = {'true': True, 'false': False, 'yes': True, 'no': False, "it's impossible to say": False}
    if predict in label_map:
        return label_map[predict]
    else:
        print(f"Alert!!! wrong answer mapping: {predict}")
        return random.sample([True, False], 1)[0]


def get_verify_result(sub_claims, evidence, qa_model, retrieve_model):
    if evidence is None:
        evidences = [retrieve_evidence(claim, retrieve_model)[0] for claim in sub_claims]
    else:
        evidences = [evidence for _ in range(len(sub_claims))]
    evidences = filter(sub_claims, evidences)
    verify_results = None
    output_texts = [qa_model.answer_verify_question(claim, e)['answer_text'] for claim, e in zip(sub_claims, evidences)]
    verify_results = [map_direct_answer_to_label(text) for text in output_texts]
    return verify_results


def decompose_then_check(claim, evidence):
    sub_claims = get_sub_claims(claim)
    verify_results = get_verify_result(sub_claims, evidence)
    return sub_claims, verify_results


def conclude_result(verify_results):
    if False in verify_results:
        return 'refutes'
    else:
        return 'supports'


def run(line, args, qa_model, retrieve_model, result_queue=None, rank=-1):
    claim = line['claim']
    evidence = line['evidence'] if args.mode == 'gold' else None
    certain_claim, history_claims, ask_questions, question_answers = perceive_then_rewrite(claim, evidence, qa_model, retrieve_model)
    sub_claims, verify_results = decompose_then_check(certain_claim, evidence, qa_model, retrieve_model)
    line['certain_claim'] = certain_claim
    line['history_claims'] = history_claims
    line['ask_questions'] = ask_questions
    line['question_answers'] = question_answers
    line['sub_claims'] = sub_claims
    line['verify_results'] = verify_results
    line['prediction'] = conclude_result(verify_results)
    if rank != -1:
        result_queue.put({
            'rank': rank,
            'line': line
        })
    else:
        return line


def run_batch(inlines, args, qa_model, retrieve_model):
    threads = []
    result_queue = Queue()
    gather_result = []
    for i in range(len(inlines)):
        t = threading.Thread(target=run, args=(inlines[i], args, qa_model, retrieve_model, result_queue, i))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    while not result_queue.empty():
        gather_result.append(result_queue.get())
    assert len(gather_result) == len(inlines)
    gather_result = sorted(gather_result, key=lambda x: x['rank'])
    gather_result = [x['line'] for x in gather_result]
    return gather_result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_root', type=str, default='./data')
    parser.add_argument('--dataset', type=str, default='HOVER')
    parser.add_argument('--split', type=str, default='dev')
    parser.add_argument('--output_path', type=str, default='output')
    parser.add_argument('--multi_process', type=int, default=1)
    parser.add_argument('--local_rank', type=int, default=0)
    parser.add_argument('--batch_size', type=int, default=1)
    parser.add_argument('--mode', type=str, default='gold')
    parser.add_argument('--qa_model', type=str, default='google/flan-t5-xl')
    args = parser.parse_args()

    data = load_data(f"{args.data_root}/{args.dataset}/claim/{args.split}.json")
    length_per_rank = len(data) // args.multi_process
    print('Data Per Rank: ', length_per_rank)
    begin_index = args.local_rank*length_per_rank
    end_index = (args.local_rank+1)*length_per_rank
    data = data[begin_index:end_index]
    output_file = f'{args.dataset}_{args.mode}_rank{args.local_rank}.jsonl'
    print(f'Process Data [ {begin_index} : {end_index} ]')
    print('Writing Results to: ', output_file)
    qa_model = T5_Question_Answering(args.qa_model)
    if args.mode == 'open':
        retrieve_index = f"./data/{args.dataset}/corpus/index"
        retrieve_model = PyseriniRetriever(retrieve_index, use_bm25=True, k1=0.9, b=0.4)
    else:
        retrieve_model = None
    index = 0
    pbar = tqdm.tqdm(total=len(data))
    while index < len(data):
        inlines, index = get_mini_batch(data, index, args.batch_size)
        outlines = run_batch(inlines, args, qa_model, retrieve_model)
        with open(os.path.join(args.output_path, output_file), 'a') as f:
            for line in outlines:
                f.write(json.dumps(line) + '\n')
        pbar.update(len(outlines))


if __name__ == '__main__':
    main()
