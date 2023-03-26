import sys


z = sys.stdin.readline().strip().split()
for s in sys.stdin:
    for c in z:
        s = s.replace(c, c + ' ' + c)
    ans = [x for x in s.split()[::-1] if x[0] in z and x[-1] in z]
    if ans:
        print(max(ans, key=len))
    else:
        print()



