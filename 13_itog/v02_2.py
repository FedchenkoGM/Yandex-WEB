import argparse
import json
import csv


parser = argparse.ArgumentParser()
parser.add_argument('--filename')
parser.add_argument('--station', default='Peace')
args = parser.parse_args()

ans = []
with open(args.filename) as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        if row['station'] == args.station:
            d = {}
            d['date'] = row['date']
            d['gate'] = row['gate']
            d['ship'] = row['ship']
            ans.append(d)

with open('start.json', 'w', newline='') as f:
    json.dump(ans, f, indent=True)