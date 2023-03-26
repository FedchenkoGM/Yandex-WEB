import requests
import json


# with open('url.json') as f:
#     data = json.load(f)
#     host = data['host']
#     port = data['port']

# resp = requests.get(f'http://{host}:{port}').json()
with open('data.txt', 'r') as f:
     resp = json.load(f)

date = input()
m = 0
for a in resp:
    if a['datetime'].split()[0] >= date and a['size'] > m:
        m, s = a['size'], a['ship']

print(s)
print(m)


