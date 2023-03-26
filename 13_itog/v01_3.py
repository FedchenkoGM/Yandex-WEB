import requests
import json


with open('third.json') as f:
    data = json.load(f)
    host = data['host']
    port = data['port']

# resp = requests.get(f'http://{host}:{port}').json()
with open('data.txt', 'r') as f:
     resp = json.load(f)

date, time = input().split()
count = 0
for a in resp:
    if a['date'] < date or a['date'] == date and a['time'] <= time:
        if a['type'] == 'ascent':
            count += a['passengers']
        if a['type'] == 'descent':
            count -= a['passengers']

print(count)


