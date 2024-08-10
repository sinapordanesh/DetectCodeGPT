import sys
def line():return sys.stdin.readline().strip()

I = {}
while True:
    try:
        a,b = line().split()
        b = int(b)
        if a in I:
            I[a].append(b)
        else:
            I[a] = [b]
    except:
        break
for k in sorted(I):
    print(k)
    print(" ".join(map(str,sorted(I[k]))))