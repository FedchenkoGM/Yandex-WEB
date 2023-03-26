import requests
import json


with open('third.json') as f:
    data = json.load(f)
    host = data['host']
    port = data['port']

# resp = requests.get(f'http://{host}:{port}').json()
with open('data.txt', 'r') as f:
     resp = json.load(f)

datetime, target = input(), input()
count = 0
for a in resp:
    if a['datetime'] >= datetime and a['target'] == target:
        count += a['crew']

print(count)


