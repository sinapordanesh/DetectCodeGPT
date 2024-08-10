from heapq import heappush, heappop
import sys
def solve():
    readline = sys.stdin.readline
    write = sys.stdout.write
    N, TI = map(int, readline().split())
    A, B = readline().split()
    S = []; T = []; X = []
    L = 0
    L = 0
    NA = set()
    for i in range(N):
        a = int(readline())
        *Si, = readline().split()
        *Ti, = map(int, readline().split())
        for s in Si:
            NA.add(s)
        X.append(a)
        S.append(Si); T.append(Ti)
        L += a
    M = len(NA); L += M
    MP = {e: i for i, e in enumerate(NA)}
    G = [[] for i in range(L)]
    cur = M
    INF = 10**18
    PN = 10**9
    for i in range(N):
        a = X[i]; Si = S[i]; Ti = T[i]
        prv = v = MP[Si[0]]
        G[v].append((cur, 1))
        G[cur].append((v, TI*PN))
        cur += 1
        for j in range(a-1):
            v = MP[Si[j+1]]; t = Ti[j]
            G[v].append((cur, 1))
            G[cur].append((v, TI*PN))
            G[cur-1].append((cur, t*PN))
            G[cur].append((cur-1, t*PN))
            cur += 1
            prv = v
    D = [INF]*L
    s = MP[A]; g = MP[B]
    D[s] = 0
    que = [(0, s)]
    while que:
        cost, v = heappop(que)
        if D[v] < cost:
            continue
        for w, d in G[v]:
            if cost + d < D[w]:
                D[w] = r = cost + d
                heappush(que, (r, w))
    if D[g] == INF:
        write("-1\n")
    else:
        d, k = divmod(D[g], PN)
        write("%d %d\n" % (d-TI, k-1))
solve()
