from collections import deque
import sys
def solve():
    readline = sys.stdin.readline
    write = sys.stdout.write
    N, M, *V = map(int, readline().split())
    G = [[] for i in range(N)]
    for i in range(M):
        u, v = map(int, readline().split())
        G[u-1].append(v-1)
    def matmul(A, B):
        C = [[0]*N for i in range(N)]
        for i in range(N):
            for j in range(N):
                C[i][j] = +(sum(A[i][k] & B[k][j] for k in range(N)) > 0)
        return C

    def fast_pow(X, k):
        R = [[0]*N for i in range(N)]
        for i in range(N):
            R[i][i] = 1
        while k:
            if k & 1:
                R = matmul(R, X)
            X = matmul(X, X)
            k >>= 1
        return R
    V.sort()
    prv = 0
    ES = [[0]*N for i in range(N)]
    for v in range(N):
        for w in G[v]:
            ES[v][w] = 1
    EE = []
    ds = []
    rgs = []
    for i, k in enumerate(V):
        d = [0]*N
        rg = [[] for i in range(N)]
        ek = fast_pow(ES, k)
        EE.append(ek)
        for v in range(N):
            ts = ek[v]
            for w in range(N):
                if ts[w]:
                    d[v] += 1
                    rg[w].append(v)
        ds.append(d)
        rgs.append(rg)
    D = [0]*N
    for i in range(3):
        d = ds[i]
        for v in range(N):
            if d[v]:
                D[v] += 1
    U = [-1]*N
    U[N-1] = 0
    que = deque([N-1])
    while que:
        v = que.popleft()
        u = U[v]
        for i, rg in enumerate(rgs):
            d = ds[i]
            for w in rg[v]:
                if d[w] == 0:
                    continue
                d[w] = 0
                D[w] -= 1
                if D[w] == 0:
                    if U[w] == -1:
                        U[w] = u+1
                        que.append(w)
    write("%d\n" % U[0] if U[0] != -1 else "IMPOSSIBLE\n")
solve()
