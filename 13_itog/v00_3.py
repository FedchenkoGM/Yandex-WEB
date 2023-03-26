import requests
import json
import datetime as dt


with open('light.json') as f:
    data = json.load(f)
    host = data['host']
    port = data['port']

# response = requests.get(f'http://{host}:{port}').json()
with open('data.txt', 'r') as f:
     response = json.load(f)

date = input()
ans = []
for a in response:
    d = dt.datetime.strptime(a['date'], '%Y/%m/%d %H:%M') + dt.timedelta(hours=a['rest_time'])
    d = d.date().strftime('%Y/%m/%d')
    if d == date:
        ans.append(a['ship'])
for ship in sorted(ans):
    print(ship)


