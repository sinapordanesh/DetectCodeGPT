# Reference: https://tjkendev.github.io/procon-library/python/min_cost_flow/primal-dual.html
from heapq import heappush, heappop
class MinCostFlow:
    INF = 10**18

    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap, cost):
        forward = [to, cap, cost, None]
        backward = forward[3] = [fr, 0, -cost, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def flow(self, s, t, f):
        N = self.N; G = self.G
        INF = MinCostFlow.INF

        res = 0
        H = [0]*N
        prv_v = [0]*N
        prv_e = [None]*N

        d0 = [INF]*N
        dist = [INF]*N

        while f:
            dist[:] = d0
            dist[s] = 0
            que = [(0, s)]

            while que:
                c, v = heappop(que)
                if dist[v] < c:
                    continue
                r0 = dist[v] + H[v]
                for e in G[v]:
                    w, cap, cost, _ = e
                    if cap > 0 and r0 + cost - H[w] < dist[w]:
                        dist[w] = r = r0 + cost - H[w]
                        prv_v[w] = v; prv_e[w] = e
                        heappush(que, (r, w))
            if dist[t] == INF:
                return None

            for i in range(N):
                H[i] += dist[i]

            d = f; v = t
            while v != s:
                d = min(d, prv_e[v][1])
                v = prv_v[v]
            f -= d
            res += d * H[t]
            v = t
            while v != s:
                e = prv_e[v]
                e[1] -= d
                e[3][1] += d
                v = prv_v[v]
        return res

###

# source >>> 1~n rows >>> (1,1)~(n,n) squares >>> 1~n columns >>> sink

from sys import stdin
input = stdin.buffer.readline

def main():
    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    mcf = MinCostFlow(n*(n+2) + 2)

    source = n*(n+2)
    sink = n*(n+2) + 1

    # add edges
    #source >>> sink
    mcf.add_edge(source, sink, n*k, 0)

    for i in range(n):
        # source >>> rows
        mcf.add_edge(source, n*n + i, k, 0)
        # columns >>> sink
        mcf.add_edge(n*(n+1) + i, sink, k, 0)

        for j in range(n):
            # rows >>> squares
            mcf.add_edge(n*n + i, n*i + j, 1, -a[i][j])
            # squares >>> columns
            mcf.add_edge(n*i + j, n*(n+1) + j, 1, 0)

    print(-mcf.flow(source, sink, n*k))

    ans = [['.'] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if mcf.G[n*i + j][0][1]:
                ans[i][j] = 'X'

    for row in ans:
        print(''.join(row))

main()