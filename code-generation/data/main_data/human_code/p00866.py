from itertools import permutations
BASE = 12*3600
def convert(v):
    return "%02d:%02d:%02d" % (v // 3600, (v // 60) % 60, v % 60)
while 1:
    N = int(input())
    if N == 0:
        break
    R = set()
    L = []
    for i in range(N):
        ts = set()
        *E, = map(int, input().split())
        for a, b, c in permutations(E, r=3):
            for i in range(60):
                h = (a+i) % 60; m = (b+i)%60; s = (c+i) % 60
                if m // 12 == h % 5:
                    v = 3600*(h//5) + 60*m + s
                    ts.add(v)
                    R.add(v)
        L.append(sorted(ts))
    R = sorted(R)
    res = 13*3600; mi = ma = 0
    C = [0]*N
    for r in R:
        s = r
        for i in range(N):
            c = C[i]; ts = L[i]; l = len(ts)
            while c < l and ts[c] < r:
                c += 1
            C[i] = c
            if c == l:
                s = max(s, BASE + ts[0])
            else:
                s = max(s, ts[c])
        if s - r < res:
            res = s - r
            mi = r % BASE; ma = s % BASE
    print("%s %s" % (convert(mi), convert(ma)))
