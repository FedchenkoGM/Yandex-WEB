import argparse
import json
import csv


parser = argparse.ArgumentParser()
parser.add_argument('--file')
parser.add_argument('--param', default='time')
parser.add_argument('--maximum', default=10)
args = parser.parse_args()

ans = []
with open(args.file) as f:
    reader = csv.DictReader(f, delimiter=':')
    for row in reader:
        if int(row[args.param]) <= int(args.maximum):
            d = {}
            d['expert'] = row['expert']
            d['size'] = int(row['size'])
            d['time'] = int(row['time'])
            d['count'] = int(row['count'])
            ans.append(d)

with open('result.json', 'w', newline='') as f:
    json.dump(ans, f, indent=True)
