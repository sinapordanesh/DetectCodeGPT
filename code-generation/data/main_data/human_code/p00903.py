from heapq import heappush, heappop
from collections import defaultdict
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N, M = map(int, readline().split())
    if N == M == 0:
        return False
    D = [0]*N; E = [0]*N
    B = [0]*N
    H = defaultdict(int)
    H[0] = 1
    H[1000] += 1
    E[N-1] = 1000
    for i in range(1, N-1):
        D[i], e = map(int, readline().split())
        E[i] = e
        B[i] = H[e]
        H[e] += 1

    G = [[] for i in range(N)]
    RG = [[] for i in range(N)]
    for i in range(M):
        a, b, c = map(int, readline().split()); a -= 1; b -= 1
        if E[a] <= E[b]:
            G[a].append((b, c))
        if E[b] <= E[a]:
            RG[b].append((a, c))
    dist = {(0, 0, 1): 0}
    que = [(0, 0, 0, 1)]
    INF = 10**18
    while que:
        cost, v0, v1, state = heappop(que)
        if dist[v0, v1, state] < cost:
            continue
        d0 = E[v0]; d1 = E[v1]
        if d0 < d1:
            for w0, d in G[v0]:
                if E[w0] == d1:
                    if w0 == v1:
                        de = cost + d
                        n_state = (1 << B[w0])
                    else:
                        de = cost + d + D[w0]
                        n_state = (1 << B[w0]) | (1 << B[v1])
                    n_key = (w0, v1, n_state)
                    if de < dist.get(n_key, INF):
                        dist[n_key] = de
                        heappush(que, (de, w0, v1, n_state))
                else:
                    n_key = (w0, v1, 0)
                    de = cost + d + D[w0]
                    if de < dist.get(n_key, INF):
                        dist[n_key] = de
                        heappush(que, (de, w0, v1, 0))
        elif d0 > d1:
            for w1, d in RG[v1]:
                if E[w1] == d0:
                    if w1 == v0:
                        de = cost + d
                        n_state = (1 << B[w1])
                    else:
                        de = cost + d + D[w1]
                        n_state = (1 << B[w1]) | (1 << B[v0])
                    n_key = (v0, w1, n_state)
                    if de < dist.get(n_key, INF):
                        dist[n_key] = de
                        heappush(que, (de, v0, w1, n_state))
                else:
                    n_key = (v0, w1, 0)
                    de = cost + d + D[w1]
                    if de < dist.get(n_key, INF):
                        dist[n_key] = de
                        heappush(que, (de, v0, w1, 0))
        else:
            ds = d0
            for w0, d in G[v0]:
                if ds == E[w0]:
                    b = (1 << B[w0])
                    if state & b:
                        de = cost + d
                        n_state = state
                    else:
                        de = cost + d + D[w0]
                        n_state = state | b
                    n_key = (w0, v1, n_state)
                    if de < dist.get(n_key, INF):
                        dist[n_key] = de
                        heappush(que, (de, w0, v1, n_state))
                else:
                    n_key = (w0, v1, 0)
                    de = cost + d + D[w0]
                    if de < dist.get(n_key, INF):
                        dist[n_key] = de
                        heappush(que, (de, w0, v1, 0))
            for w1, d in RG[v1]:
                if ds == E[w1]:
                    b = (1 << B[w1])
                    if state & b:
                        de = cost + d
                        n_state = state
                    else:
                        de = cost + d + D[w1]
                        n_state = state | b
                    n_key = (v0, w1, n_state)
                    if de < dist.get(n_key, INF):
                        dist[n_key] = de
                        heappush(que, (de, v0, w1, n_state))
                else:
                    n_key = (v0, w1, 0)
                    de = cost + d + D[w1]
                    if de < dist.get(n_key, INF):
                        dist[n_key] = de
                        heappush(que, (de, v0, w1, 0))
    g_key = (N-1, N-1, 1)
    if g_key in dist:
        write("%d\n" % dist[g_key])
    else:
        write("-1\n")
    return True
while solve():
    ...
