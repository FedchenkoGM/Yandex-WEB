import argparse
import json
import csv


parser = argparse.ArgumentParser()
parser.add_argument('--star')
parser.add_argument('--param', default='life')
args = parser.parse_args()

ans = []
with open('planets.csv') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        if row['star'] == args.star and row[args.param] in ('True', '1'):
            d = {}
            d['planet'] = row['planet']
            d['oxygen'] = row['oxygen']
            d['atmosphere'] = row['atmosphere']
            d['water'] = row['water']
            d['life'] = row['life']
            ans.append(d)

with open('choice.json', 'w', newline='') as f:
    json.dump(ans, f, indent=True)