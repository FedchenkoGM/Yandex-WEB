import sys


z = sys.stdin.readline().strip()
for s in sys.stdin:
    for c in z:
        s = s.replace(c, ' ')
    a = s.split()
    if a:
        m = max(len(x) for x in a)
        ans = [x for x in a if len(x) == m]
        print(min(ans))
    else:
        print()



