import requests
import json


with open('space_life.json') as f:
    data = json.load(f)
    host = data['host']
    port = data['port']

# resp = requests.get(f'http://{host}:{port}').json()
with open('data.json', 'r') as f:
     resp = json.load(f)

date, bright = input(), int(input())
count = 0
for key in resp:
    if resp[key]['beginning'] <= date <= resp[key]['end'] and int(resp[key]['brightness']) >= bright:
        count += 1

print(count)

