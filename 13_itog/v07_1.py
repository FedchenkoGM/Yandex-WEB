import sys


def work(z, s):
    t = []
    for i in range(len(s)):
        if s[i] in z:
            t.append(i)
    mi = 10**10
    if len(t) > 2:
        for i in range(len(t) - 2):
            if t[i + 2] - t[i] < mi:
                mi = t[i + 2] - t[i]
    return mi + 1


z = sys.stdin.readline().strip()
ans = set()
for s in sys.stdin:
    ans.add(work(z, s.strip()))
print(' '.join(str(x) for x in ans))


