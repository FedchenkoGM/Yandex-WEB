import argparse
import json
import csv


parser = argparse.ArgumentParser()
parser.add_argument('--filename')
parser.add_argument('--relevance', default=3)
args = parser.parse_args()

ans = []
with open(args.filename) as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        if int(row['relevance']) >= int(args.relevance):
            d = {}
            d['length'] = int(row['length'])
            d['target'] = row['target']
            d['relevance'] = int(row['relevance'])
            ans.append(d)

with open('importance.json', 'w', newline='') as f:
    json.dump(ans, f, indent=True)