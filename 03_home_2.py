import sys


data = sys.argv[1:]
fsort = False
if data[0] == '--sort':
    fsort = True
    data = data[1:]
params = {}
for p in data:
    if p == '--sort':
        fsort = True
    else:
        key, value = p.split('=')
        params[key] = value
keys = params.keys()
if fsort:
    keys = sorted(keys)
for p in keys:
    print(f'Key: {p} Value: {params[p]}')