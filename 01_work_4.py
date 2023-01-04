import json


with open('scoring.json') as f:
    data = json.load(f)
score = 0
for block in data['scoring']:
    k = 0
    n = len(block['required_tests'])
    for i in range(n):
        if input() == 'ok':
            k += 1
    score += k * block['points'] // n
print(score)






