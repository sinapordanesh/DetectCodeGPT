import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from heapq import heappop, heappush
import itertools

"""
・最小費用流。流量2を流せばよい。
・頂点xをx_in,x_outに拡張。x_inからx_outにcapacity1で、価値 a と 0 の辺を貼る
・このままだと最大化問題になっているので、辺のコストをX - a_{ij}とする感じで
"""

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
            if dist[sink] == INF:
                raise Exception('No Flow Exists')
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

H,W = map(int,readline().split())
A = list(map(int,read().split()))

N = 2 * H * W + 2
source = N-2; sink = N-1

G = MinCostFlow(N,source,sink)
add = G.add_edge
X = 10 ** 6

# スタート地点
add(fr=source, to=0, cap=2, cost=0)
# ゴール
add(2*H*W-1, sink, 2, 0)

# x_in to x_out
for x,a in enumerate(A):
    add(x+x,x+x+1,1,X) # とらない
    add(x+x,x+x+1,1,X - a) # とる

# 左から右への辺
for i,j in itertools.product(range(H),range(W-1)):
    x = W * i + j; y = x + 1
    add(x+x+1,y+y,1,0)
# 上から下への辺
for i,j in itertools.product(range(H-1),range(W)):
    x = W * i + j; y = x + W
    add(x+x+1,y+y,1,0)

cost = G.MinCost(2)

# 1点通るごとに、X - costになっている。2人合わせて、(H+W-1) * 2個のXが足されている

answer = 2 * (H+W-1) * X -cost
print(answer)