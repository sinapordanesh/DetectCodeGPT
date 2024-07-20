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

from sys import stdin
def input():
    return stdin.readline().strip()

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]

    mcf = MinCostFlow(n*m + 2)

    source = n * m
    sink = n * m + 1

    ans = 0
    cnt = 0
    for i in range(n):
        for j in range(m):
            if s[i][j] == '#':
                continue

            ind = m * i + j

            # source >>> 'o'
            if s[i][j] == 'o':
                ans -= i + j
                cnt += 1
                mcf.add_edge(source, ind, 1, 0)

            mcf.add_edge(ind, sink, 1, -i-j)

            if i < n - 1 and s[i+1][j] != '#':
                mcf.add_edge(ind, m*(i+1) + j, 100, 0)
            if j < m - 1 and s[i][j+1] != '#':
                mcf.add_edge(ind, m*i + j+1, 100, 0)

    print(ans - mcf.flow(source, sink, cnt))

main()