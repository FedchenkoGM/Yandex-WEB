import sys

n = int(input())
shablon = input()

for s in sys.stdin:
    ind = []
    for i in range(len(s)):
        if s[i] in shablon:
            ind.append(i)

    if ind:
        m, t = 1, 1
        start = finish = ind[0]
        start_t = start
        for i in range(len(ind) - 1):
            if ind[i + 1] - ind[i] <= n:
                t += (ind[i + 1] - ind[i])
                if t > m:
                    m = t
                    start = start_t
                    finish = ind[i + 1]
            else:
                t = 1
                start_t = ind[i + 1]

        print(s[start:finish + 1])
    else:
        print()
