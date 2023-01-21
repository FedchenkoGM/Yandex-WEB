import sys


data = sys.argv[1:]
if not data:
    print("NO PARAMS")
else:
    try:
        z, s = 1, 0
        for a in data:
            s += z * int(a)
            z *= -1
        print(s)
    except Exception as ex:
        print(ex.__class__.__name__)