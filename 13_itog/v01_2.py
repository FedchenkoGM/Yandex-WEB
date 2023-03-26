import argparse
import json
import csv


parser = argparse.ArgumentParser()
parser.add_argument('--param')
parser.add_argument('--smallest', default=0)
args = parser.parse_args()

ans = []
with open('ships.csv') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        if int(row[args.param]) >= int(args.smallest):
            d = {}
            d['name'] = row['name']
            d['year'] = row['year']
            d['load'] = row['load']
            d['crew'] = row['crew']
            d['distance'] = row['distance']
            d['engines'] = row['engines']
            ans.append(d)

with open('toys.json', 'w', newline='') as f:
    json.dump(ans, f, indent=True)