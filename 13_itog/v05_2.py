import argparse
import json
import csv


parser = argparse.ArgumentParser()
parser.add_argument('--place')
parser.add_argument('--number', default=2)
args = parser.parse_args()

ans = []
with open('infinity.csv') as f:
    reader = csv.DictReader(f, delimiter='_')
    for row in reader:
        if row['place'] == args.place and len(row['members'].split(',')) >= int(args.number):
            d = {}
            d['date'] = int(row['date'])
            d['name'] = row['name']
            d['tag'] = row['tag']
            ans.append(d)

with open('memories.json', 'w', newline='') as f:
    json.dump(ans, f, indent=True)