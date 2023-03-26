import requests
import json


with open('space_life.json') as f:
    data = json.load(f)
    host = data['host']
    port = data['port']

# resp = requests.get(f'http://{host}:{port}').json()
with open('data.json', 'r') as f:
     resp = json.load(f)

type, date = input(), input()
ans = set()
for key in resp:
    if key <= date:
        for d in resp[key]:
            if d['type'] == type:
                ans.add(d['galaxy'])

print(', '.join(x for x in sorted(ans)))

