import sys

shablon = set(input())

for s in sys.stdin:
    m = len(s) + 1
    for i in range(len(s) - len(shablon) + 1):
        for j in range(i, len(s) + 1):
            if set(s[i:j]) & shablon == shablon:
                if j - i < m:
                    m = j - i
                    ans = s[i:j]
                    break
    if m < len(s) + 1:
        print(ans)
    else:
        print()
