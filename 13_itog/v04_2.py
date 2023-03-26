import argparse
import json
import csv


parser = argparse.ArgumentParser()
parser.add_argument('--file')
parser.add_argument('--motor', default='puls')
args = parser.parse_args()

ans = {}
with open(args.file) as f:
    reader = csv.DictReader(f, delimiter=':')
    for row in reader:
        if row['motor'] == args.motor:
            ans[row['ship']] = [row['start'], row['destination']]


with open('destinations.json', 'w', newline='') as f:
    json.dump(ans, f, indent=True)