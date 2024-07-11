from collections import deque
from heapq import heappop, heappush
def inpl(): return list(map(int, input().split()))

INF = 50000

N, M = inpl()
while N:
    s, g = inpl()
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, d, c = inpl()
        G[a].append([b, c, d])
        G[b].append([a, c, d])
    DP =  [[[INF]*(N+1) for _ in range(31)] for _ in range(N+1)]
    DP[s][0][0] = 0
    Q = [[0, 0, s, 0]]  # time, speed, where, pre
    while Q:
        t, v, p, bp = heappop(Q)
        if DP[p][v][bp] < t:
            continue
        for q, c, d in G[p]:
            if q == bp:
                continue

            for dv in range(-1, 2):
                nv = v+dv
                if not (0 < nv <= c):
                    continue
                nt = t + d/(nv)
                if DP[q][nv][p] > nt:
                    DP[q][nv][p] = nt
                    heappush(Q, [nt, nv, q, p])

    ans = min(DP[g][1])
    if ans == INF:
        print("unreachable")
    else:
        print(ans)
    N, M = inpl()

