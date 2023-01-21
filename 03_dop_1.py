import sys


data = sys.argv[1:]
fsort = fnum = fcount = False
if '--sort' in data:
    fsort = True
    data.remove('--sort')
if '--count' in data:
    fcount = True
    data.remove('--count')
if '--num' in data:
    fnum = True
    data.remove('--num')

try:
    f = open(data[0])
    text = f.readlines()
    f.close()
    if fsort:
        text = sorted(text)
    for i, row in enumerate(text):
        if fnum:
            print(i, end=' ')
        print(row.strip())
    if fcount:
        print(f'rows count: {i + 1}')

except Exception:
    print('ERROR')