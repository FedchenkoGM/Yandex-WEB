import sys


z = sys.stdin.readline().strip()
ans = []
for s in sys.stdin:
    for c in s:
        if not c in z:
            s = s.replace(c, ' ')
#    print(s.split())
    if s.split():
        ans.append(max(s.split(), key = len))
#print(ans)
print(max(ans))



