from collections import defaultdict
import sys
def solve():
    readline = sys.stdin.readline
    write = sys.stdout.write
    f = "<v>^".index
    N = int(readline())
    Y = defaultdict(list)
    for i in range(N):
        x, y, d = readline().split()
        x = int(x); y = int(y)
        Y[y].append((x, f(d)))
    *S, = Y.items()
    S.sort()
    L = [0]*N
    V = [[-1]*4 for i in range(N)]
    cur = 0
    X = {}
    for y, es in S:
        es.sort()
        prv = -1
        for x, d in es:
            v = V[cur]
            L[cur] = d
            if x in X:
                k = X[x]
                v[3] = k
                V[k][1] = cur
            X[x] = cur
            if prv != -1:
                v[0] = prv
                V[prv][2] = cur
            prv = cur
            cur += 1
    ans = 0
    for i in range(N):
        res = 0
        R = [e[:] for e in V]
        v = i
        while v != -1:
            d = L[v]
            w0, w1, w2, w3 = r = R[v]
            if w0 != -1:
                R[w0][2] = w2
            if w1 != -1:
                R[w1][3] = w3
            if w2 != -1:
                R[w2][0] = w0
            if w3 != -1:
                R[w3][1] = w1
            res += 1
            v = r[d]
        ans = max(ans, res)
    write("%d\n" % ans)
solve()
