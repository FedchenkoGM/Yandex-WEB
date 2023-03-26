import sys


z = sys.stdin.readline().strip()
ans = set()
for s in sys.stdin:
    for c in z:
        s = s.replace(c, c + ' ' + c)
    t = [len(x) for x in s.split() if x[0] in z and x[-1] in z and len(x) > 1]
    if t:
        ans.add(min(t))
ans = sorted(ans)
print(', '.join(str(x) for x in ans))



