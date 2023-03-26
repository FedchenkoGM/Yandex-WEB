import requests
import json


with open('space_life.json') as f:
    data = json.load(f)
    host = data['host']
    port = data['port']

# resp = requests.get(f'http://{host}:{port}').json()
with open('data.json', 'r') as f:
     resp = json.load(f)

spec, date = input(), input()
ans = []
for key in resp:
    if resp[key]['specialization'] == spec and resp[key]['date'] <= date:
        ans.append((key, resp[key]['title']))

for x in sorted(ans):
    print(*x)

