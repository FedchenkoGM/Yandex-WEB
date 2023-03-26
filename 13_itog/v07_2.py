import argparse
import json
import csv


parser = argparse.ArgumentParser()
parser.add_argument('--file')
parser.add_argument('--type', default='elliptical')
args = parser.parse_args()

ans = []
with open(args.file) as f:
    reader = csv.DictReader(f, delimiter=':')
    ans = {}
    for row in reader:
        if row['type'] == args.type:
            a = int(row['dark']) / int(row['mass'])
            ans[row['galaxy']] = f'{a:.1f}'


with open('relations.json', 'w', newline='') as f:
    json.dump(ans, f, indent=True)