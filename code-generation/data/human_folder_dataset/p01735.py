from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N = int(readline())
    *P, = map(int, readline().split())
    G = []
    prt = [0]*N
    for i in range(N):
        k, *t = map(int, readline().split())
        G.append([e-1 for e in t])
        for e in t:
            prt[e-1] = i
    *D, = map(len, G)
    A = [0]*N
    deg = D[:]
    que = deque()
    for v in range(N):
        if deg[v] == 0:
            A[v] = P[v]
            que.append(v)
    while que:
        v = que.popleft()
        p = prt[v]
        deg[p] -= 1
        if deg[p] == 0:
            A[p] = max(-A[w] for w in G[p])
            que.append(p)

    for v in range(N):
        if D[v] == 0:
            A[v] = P[v]
        else:
            A[v] = max(-A[w] for w in G[v])

    memo = {}
    def dfs(v, state, c, a, b):
        key = (v, state, a, b)
        if key in memo:
            return memo[key]
        if c == D[v]:
            if c == 0:
                return 1, 1
            return 0, 0
        c0 = N+1; c1 = 0
        Gv = G[v]
        for k in range(D[v]):
            if state & (1 << k):
                continue
            w = Gv[k]
            s0, s1 = dfs(w, 0, 0, -b, -a)
            val = -A[w]
            if val >= b:
                c0 = min(c0, s0); c1 = max(c1, s1)
                continue
            t0, t1 = dfs(v, state | (1 << k), c+1, max(a, val), b)
            c0 = min(c0, s0+t0)
            c1 = max(c1, s1+t1)
        memo[key] = c0, c1
        return c0, c1
    INF = 10**9
    r0, r1 = dfs(0, 0, 0, -INF, INF)
    write("%d %d\n" % (r0, r1))
solve()
