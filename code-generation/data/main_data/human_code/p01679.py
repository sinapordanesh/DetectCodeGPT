from heapq import heappush, heappop
import sys
def main():
    readline = sys.stdin.readline
    write = sys.stdout.write
    L2 = 1 << 16
    bc = [0]*L2
    for i in range(1, L2):
        bc[i] = bc[i ^ (i & -i)] + 1
    INF = 10**18
    def solve():
        N, M, L, s, T = map(int, readline().split())
        if N == M == 0:
            return False
        G = [[] for i in range(N)]
        for i in range(M):
            a, b, c = map(int, readline().split()); a -= 1; b -= 1
            G[a].append((b, c))
            G[b].append((a, c))
        def dijkstra(s):
            dist = [INF]*N
            dist[s] = 0
            que = [(0, s)]
            while que:
                cost, v = heappop(que)
                if dist[v] < cost:
                    continue
                for w, d in G[v]:
                    if cost + d < dist[w]:
                        dist[w] = cost + d
                        heappush(que, (cost + d, w))
            return dist

        G0 = [[] for i in range(L)]
        RS = []
        BS = [0]*L
        for i in range(L):
            j, e = map(int, readline().split()); j -= 1
            d0 = dijkstra(j)
            for k, p in enumerate(RS):
                v = d0[p]
                if v+BS[k] <= T:
                    G0[i].append((k, v+BS[k], 1 << k))
                if v+e <= T:
                    G0[k].append((i, v+e, 1 << i))
            RS.append(j)
            BS[i] = e

        ans = 0
        ds = dijkstra(s-1)
        que = []
        Q = [[{} for j in range(L)] for i in range(L+1)]
        L2 = 1 << L
        dw = [0]*L
        for i in range(L):
            d = ds[RS[i]]
            r = d + BS[i]
            dw[i] = T - d + 1
            if r < dw[i]:
                Q[1][i][1 << i] = r
                ans = 1
        for k in range(1, L):
            qs = Q[k]
            qs1 = Q[k+1]
            if any(qs):
                ans = k
            for v in range(L):
                qsv = qs[v]
                for w, d, b in G0[v]:
                    dww = dw[w]
                    qs1w = qs1[w]
                    for state, cost in qsv.items():
                        if state & b:
                            continue
                        r = cost + d
                        if r < qs1w.get(state | b, dww):
                            qs1w[state | b] = r
        if any(Q[L]):
            ans = L
        write("%d\n" % ans)
        return True
    while solve():
        ...
main()
