import json


def load_data(file_name):
    with open(file_name, 'r') as fin:
        if '.jsonl' in file_name:
            lines = fin.readlines()
            data = [json.loads(line) for line in lines]
        else:
            data = json.load(fin)
    return data


def get_mini_batch(data, index, batch_size):
    begin = index
    end = min(len(data), index + batch_size)
    return data[begin:end], end
