import argparse
import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration


class T5_Question_Answering:
    def __init__(self, model_name):
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)
        # self.model.parallelize()

    def generate(self, input_string, **generator_args):
        device = "cuda:0" if torch.cuda.is_available() else "cpu"
        input_ids = self.tokenizer.encode(input_string, return_tensors="pt").to(device)
        with torch.no_grad():
            res = self.model.generate(input_ids, **generator_args)
        return self.tokenizer.batch_decode(res, skip_special_tokens=True)

    def answer_question_directly(self, question, evidence, claim_only=False):
        if claim_only == True:
            example = f"Question: {question}\nThe answer is:"
        else:
            example = f"{evidence}\nQuestion: {question}\nThe answer is:"

        # answer question with FLAN-T5
        predict_answer = {}
        answer_text = self.generate(example,
                                    max_new_tokens=32)[0].strip()

        predict_answer['rationale'] = ""
        predict_answer['answer_text'] = answer_text
        return predict_answer

    def answer_verify_question(self, claim, evidence, claim_only=False):
        claim = claim[:-1] if claim.endswith('.') else claim
        example = None
        if claim_only == True:
            example = f"Is it true that {claim}? True or false? The answer is: "
        else:
            example = f"{evidence}\nBased on the above information, is it true that {claim}? True or false? The answer is: "

        # answer question with FLAN-T5
        predict_answer = {}
        answer_text = self.generate(example,
                                    max_new_tokens=8, output_scores=True)[0].strip()

        predict_answer['rationale'] = ""
        predict_answer['answer_text'] = answer_text
        return predict_answer


