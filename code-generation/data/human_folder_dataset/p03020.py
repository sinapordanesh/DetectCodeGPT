import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from heapq import heappop, heappush

N = int(readline())
m = map(int,read().split())
data = list(zip(m,m,m))
R = data[:N]
B = data[N:]

class MinCostFlow:
    """
    最小費用流。負辺がないと仮定して、BellmanFordを省略している。
    """
    def __init__(self, N, source, sink):
        self.N = N
        self.G = [[] for _ in range(N)]
        self.source = source
        self.sink = sink
        
    def add_edge(self, fr, to, cap, cost):
        n1 = len(self.G[fr])
        n2 = len(self.G[to])
        self.G[fr].append([to, cap, cost, n2])
        self.G[to].append([fr, 0, -cost, n1])

    def MinCost(self, flow, negative_edge = False):
        if negative_edge:
            raise ValueError
        N = self.N; G = self.G; source = self.source; sink = self.sink
        INF = 10 ** 18
        prev_v = [0] * N; prev_e = [0] * N # 経路復元用
        H = [0] * N # potential
        mincost=0
        while flow:
            dist=[INF] * N
            dist[source]=0
            q = [source]
            mask = (1 << 20) - 1
            while q:
                x = heappop(q)
                dv = (x >> 20); v = x & mask
                if dist[v] < dv:
                    continue
                if v == sink:
                    break
                for i,(w,cap,cost,rev) in enumerate(G[v]):
                    dw = dist[v] + cost + H[v] - H[w]
                    if (not cap) or (dist[w] <= dw):
                        continue
                    dist[w] = dw
                    prev_v[w] = v; prev_e[w] = i
                    heappush(q, (dw << 20) + w)
            #if dist[sink] == INF:
            #    raise Exception('No Flow Exists')
            # ポテンシャルの更新
            for v,d in enumerate(dist):
                H[v] += d
            # 流せる量を取得する
            d = flow; v = sink
            while v != source:
                pv = prev_v[v]; pe = prev_e[v]
                cap = G[pv][pe][1]
                if d > cap:
                    d = cap
                v = pv
            # 流す
            mincost += d * H[sink]
            flow -= d
            v = sink
            while v != source:
                pv = prev_v[v]; pe = prev_e[v]
                G[pv][pe][1] -= d
                rev = G[pv][pe][3]
                G[v][rev][1] += d
                v = pv
        return mincost

source = N+N; sink = N+N+1
V1 = N+N+2; V2 = N+N+3; V3 = N+N+4; V4 = N+N+5

G = MinCostFlow(N+N+6, source = source, sink = sink)
base = 10 ** 9 * 2 # 各辺に上乗せしておく -> 最後に引く
INF = 10 ** 18

flow = 0

for i,(x,y,c) in enumerate(R):
    flow += c
    G.add_edge(fr=source, to=i, cap=c, cost=0)
    G.add_edge(i,V1,INF,base-x-y)
    G.add_edge(i,V2,INF,base-x+y)
    G.add_edge(i,V3,INF,base+x-y)
    G.add_edge(i,V4,INF,base+x+y)

for i,(x,y,c) in enumerate(B,N):
    G.add_edge(fr=i, to=sink, cap=c, cost=0)
    G.add_edge(V1,i,INF,base+x+y)
    G.add_edge(V2,i,INF,base+x-y)
    G.add_edge(V3,i,INF,base-x+y)
    G.add_edge(V4,i,INF,base-x-y)

cost = G.MinCost(flow)

answer = base * (2 * flow) - cost
print(answer)