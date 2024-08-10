import sys
from collections import Counter
readline = sys.stdin.readline

def compress(L):
    L2 = list(set(L))
    L2.sort()
    C = {v : k for k, v in enumerate(L2, 1)}
    return L2, C

def order(a, b, c, d):
    if a == b == c == d:
        return 4
    if a == c and b == d:
        return 2
    return 1


limit = 5
calc = [[None]*limit for _ in range(limit*400)]
for i in range(limit*400):
    calc[i][1] = i
    for j in range(2, limit):
        calc[i][j] = calc[i][j-1]*(i-j+1)
pp = [[pow(i, j) for j in range(10)] for i in range(10)]

N = int(readline())
C = [tuple(map(int, readline().split())) for _ in range(N)]
D = Counter()



Rot = []
for i in range(N):
    a, b, c, d = C[i]
    Rot.append((a, b, c, d))
    Rot.append((d, a, b, c))
    Rot.append((c, d, a, b))
    Rot.append((b, c, d, a))
Lc, Cr = compress(Rot)
Lc = [None] + Lc
Cc = []

Od = Counter()
Base = Counter()
D = Counter()
for i in range(N):
    a, b, c, d = C[i]
    a, b, c, d = min((a, b, c, d), (b, c, d, a), (c, d, a, b), (d, a, b, c))
    od = order(a, b, c, d)
    r1 = Cr[(a, b, c, d)]
    r2 = Cr[(b, c, d, a)]
    r3 = Cr[(c, d, a, b)]
    r4 = Cr[(d, a, b, c)]
    Base[r1] = r1
    Base[r2] = r1
    Base[r3] = r1
    Base[r4] = r1
    Od[r1] = od
    Od[r2] = od
    Od[r3] = od
    Od[r4] = od
    Cc.append((r1, r2, r3, r4))
    D[r1] += 1


ans = 0
for i in range(N):
    D[Cc[i][0]] -= 1
    a, b, c, d = Lc[Cc[i][0]]
    for j in range(i+1, N):
        D[Cc[j][0]] -= 1
        for idx in range(4):
            e, f, g, h = Lc[Cc[j][idx]]
            E = Counter()
            r1 = (b, e, h, c)
            if r1 not in Cr:
                continue
            r1 = Base[Cr[r1]]
            r2 = (a, f, e, b)
            if r2 not in Cr:
                continue
            r2 = Base[Cr[r2]]
            r3 = (d, g, f, a)
            if r3 not in Cr:
                continue
            r3 = Base[Cr[r3]]
            r4 = (c, h, g, d)
            if r4 not in Cr:
                continue
            r4 = Base[Cr[r4]]
            
            E[r1] += 1
            E[r2] += 1
            E[r3] += 1
            E[r4] += 1            
            res = 1
            for k, n in E.items():
                res *= calc[D[k]][n] * pp[Od[k]][n]
            ans += res
        
        D[Cc[j][0]] += 1

print(ans)
