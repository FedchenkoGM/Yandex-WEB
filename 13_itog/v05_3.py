import requests
import json


with open('third.json') as f:
    data = json.load(f)
    host = data['host']
    port = data['port']

# resp = requests.get(f'http://{host}:{port}').json()
with open('data.txt', 'r') as f:
     resp = json.load(f)

datetime, dir = input(), input()
ans = set()
for a in resp:
    if a['date_time'] >= datetime and a['direction'] == dir:
        ans |= set(a['frequency_list'])

print(' '.join(str(x) for x in sorted(ans)))


