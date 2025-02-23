import json

with open('claims/four_hop_ids.json', 'r') as fin:
    ids = json.load(fin)

with open('claims/dev_hop4.json', 'r') as fin:
    data = json.load(fin)

output = []
for item in ids:
    i = item['id']
    for d in data:
        if d['id'] == i:
            output.append(d)

assert len(output) == len(ids), print(len(output))
with open('claims/dev_hop4_subset.json', 'w') as fout:
    json.dump(output, fout, indent=4)
