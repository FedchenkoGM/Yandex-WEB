import argparse
import json
import csv


parser = argparse.ArgumentParser()
parser.add_argument('--file')
parser.add_argument('--criterion', default='danger')
parser.add_argument('--value', default=7)
args = parser.parse_args()

ans = []
with open(args.file) as f:
    reader = csv.DictReader(f, delimiter='.')
    for row in reader:
        if int(row[args.criterion]) <= int(args.value):
            d = {}
            d['experiment'] = row['experiment']
            d['difficulty'] = row['difficulty']
            d['duration'] = row['duration']
            d['danger'] = row['danger']
            ans.append(d)

with open('experience.json', 'w', newline='') as f:
    json.dump(ans, f, indent=True)