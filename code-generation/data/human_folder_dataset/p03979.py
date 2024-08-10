from collections import deque


class Dinic:
    def __init__(self, N, inf):
        self.N = N
        self.inf = inf
        self.G = [[] for _ in range(N)]
        self.level = [0]*N

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s):
        self.level = [-1]*self.N
        deq = deque([s])
        self.level[s] = 0
        while deq:
            v = deq.pop()
            lv = self.level[v] + 1
            for w, cap, _ in self.G[v]:
                if cap > 0 and self.level[w] == -1:
                    self.level[w] = lv
                    deq.appendleft(w)

    def dfs(self, v, t, f):
        if v == t:
            return f
        for e in self.iter[v]:
            w, cap, rev = e
            if cap > 0 and self.level[v] < self.level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d > 0:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.level[t] == -1:
                return flow
            *self.iter, = map(iter, self.G)
            f = self.inf
            while f > 0:
                f = self.dfs(s, t, self.inf)
                flow += f


import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


H,W = MI()
S = [LS2() for _ in range(H)]

Di = Dinic(2*H*W+2,10000)
s,t = 2*H*W,2*H*W+1

for i in range(H):
    for j in range(W):
        if S[i][j] == 'X':
            Di.add_edge(s,W*i+j,10000)

for j in range(W):
    Di.add_edge(H*W+j,t,10000)
    Di.add_edge(H*W+W*(H-1)+j,t,10000)
for i in range(1,H-1):
    Di.add_edge(H*W+W*i,t,10000)
    Di.add_edge(H*W+W*i+(W-1),t,10000)

for i in range(H):
    for j in range(W-1):
        Di.add_edge(H*W+W*i+j,W*i+(j+1),10000)
        Di.add_edge(H*W+W*i+(j+1),W*i+j,10000)
for i in range(H-1):
    for j in range(W):
        Di.add_edge(H*W+W*i+j,W*(i+1)+j,10000)
        Di.add_edge(H*W+W*(i+1)+j,W*i+j,10000)

for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            Di.add_edge(W*i+j,H*W+W*i+j,1)
        else:
            Di.add_edge(W*i+j,H*W+W*i+j,10000)

flow = Di.flow(s,t)
print(flow if flow < 10000 else -1)
