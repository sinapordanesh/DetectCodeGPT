import sys
readline = sys.stdin.readline
write = sys.stdout.write
from collections import deque
INF = 10**9
def bfs(N, G, s):
    dist = [INF]*N
    *lb, = range(N)
    dist[s] = 0
    que = deque([s])
    while que:
        v = que.popleft()
        d = dist[v] + 1
        l = lb[v]
        for w in G[v]:
            if dist[w] == INF:
                dist[w] = d
                lb[w] = min(l, lb[w])
                que.append(w)
            elif dist[w] == d:
                lb[w] = min(l, lb[w])
    return dist, lb
def solve():
    N, A, B, C = map(int, readline().split())
    *LS, = range(N)
    *LA, = map(int, readline().split())
    ga = min(LA)-1
    for i in LA:
        LS[i-1] = ga
    *LB, = map(int, readline().split())
    gb = min(LB)-1
    for i in LB:
        LS[i-1] = gb
    *LC, = map(int, readline().split())
    gc = min(LC)-1
    for i in LC:
        LS[i-1] = gc
    G = [set() for i in range(N)]
    M = int(readline())
    for i in range(M):
        x, y = map(int, readline().split())
        lx = LS[x-1]; ly = LS[y-1]
        G[lx].add(ly); G[ly].add(lx)
    da, la = bfs(N, G, ga)
    db, lb = bfs(N, G, gb)
    dc, lc = bfs(N, G, gc)
    ans = INF; k = -1
    for i in range(N):
        d = da[i] + db[i] + dc[i]
        if d <= ans:
            l = min(la[i], lb[i], lc[i])
            if d < ans:
                ans = d
                k = l
            else:
                k = min(l, k)
    write("%d %d\n" % (ans, k+1))
solve()
