import requests
import json


with open('third.json') as f:
    data = json.load(f)
    host = data['host']
    port = data['port']

# resp = requests.get(f'http://{host}:{port}').json()
with open('data.txt', 'r') as f:
     resp = json.load(f)

datetime = input()
m = 0
for a in resp:
    if a['date'] + ' ' + a['time'] >= datetime and a['participants'] > m:
        m, event = a['participants'], a['event']

print(event)
print(m)


