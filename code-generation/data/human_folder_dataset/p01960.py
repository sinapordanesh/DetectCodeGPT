from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N, K = map(int, readline().split())
    G = [[] for i in range(N)]
    for i in range(N-1):
        u, v = map(int, readline().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    P = [-1]*N
    vs = []
    que = deque([0])
    used = [0]*N
    used[0] = 1
    while que:
        v = que.popleft()
        vs.append(v)
        for w in G[v]:
            if used[w]:
                continue
            used[w] = 1
            que.append(w)
            P[w] = v
    sz = [0]*N; dp = [0]*N
    vs.reverse()
    ans = 0
    for v in vs:
        s = 1; d = 0
        p = P[v]
        ds = []
        for w in G[v]:
            if w == p:
                continue
            s += sz[w]
            if sz[w] >= K:
                d += 1
                ds.append(dp[w]-1)
            else:
                ds.append(dp[w])
        ds.sort(reverse=1)
        dp[v] = max(d, d + ds[0] if ds else 0)
        if ds:
            e = d + 1 if N-s >= K else d
            ans = max(ans, e + ds[0])
            if len(ds) > 1:
                ans = max(ans,  e + ds[0] + ds[1])
        sz[v] = s
    write("%d\n" % ans)
solve()
