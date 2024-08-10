import sys
from heapq import heappush, heappop
readline = sys.stdin.buffer.readline
write = sys.stdout.write

def solve():
    N, M, C = map(int, readline().split())
    if N == M == C == 0:
        return False
    G = [[] for i in range(N)]
    for i in range(M):
        f, t, c = map(int, readline().split()); f -= 1; t -= 1
        G[f].append((t, c))
    INF = 10**18
    dist = [[INF]*(N+1) for i in range(N)]
    que = [(0, 0, 0)]
    dist[0][0] = 0
    while que:
        cost, v, k = heappop(que)
        if dist[v][k] < cost:
            continue
        for w, d in G[v]:
            if cost + d < dist[w][k]:
                dist[w][k] = cost + d
                heappush(que, (cost + d, w, k))
            if k < N and cost < dist[w][k+1]:
                dist[w][k+1] = cost
                heappush(que, (cost, w, k+1))
    for k in range(N+1):
        if dist[N-1][k] <= C:
            write("%d\n" % k)
            break
    return True

while solve():
    ...

