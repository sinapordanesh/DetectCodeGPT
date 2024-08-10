import sys
readline = sys.stdin.readline
write = sys.stdout.write

from collections import deque
class HopcroftKarp:
    def __init__(self, N0, N1):
        self.N0 = N0
        self.N1 = N1
        self.N = N = 2+N0+N1
        self.G = [[] for i in range(N)]
        for i in range(N0):
            forward = [2+i, 1, None]
            forward[2] = backward = [0, 0, forward]
            self.G[0].append(forward)
            self.G[2+i].append(backward)
        self.backwards = bs = []
        for i in range(N1):
            forward = [1, 1, None]
            forward[2] = backward = [2+N0+i, 0, forward]
            bs.append(backward)
            self.G[2+N0+i].append(forward)
            self.G[1].append(backward)

    def add_edge(self, fr, to):
        #assert 0 <= fr < self.N0
        #assert 0 <= to < self.N1
        v0 = 2 + fr
        v1 = 2 + self.N0 + to
        forward = [v1, 1, None]
        forward[2] = backward = [v0, 0, forward]
        self.G[v0].append(forward)
        self.G[v1].append(backward)

    def bfs(self):
        G = self.G
        level = [None]*self.N
        deq = deque([0])
        level[0] = 0
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        self.level = level
        return level[1] is not None

    def dfs(self, v, t):
        if v == t:
            return 1
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w] and self.dfs(w, t):
                e[1] = 0
                rev[1] = 1
                return 1
        return 0

    def flow(self):
        flow = 0
        G = self.G
        bfs = self.bfs; dfs = self.dfs
        while bfs():
            *self.it, = map(iter, G)
            while dfs(0, 1):
                flow += 1
        return flow

    def matching(self):
        return [cap for _, cap, _ in self.backwards]

def solve():
    N, M, L = map(int, readline().split())
    if N == 0:
        return False
    INF = 10**9
    E = [[INF]*N for i in range(N)]
    for i in range(M):
        u, v, d = map(int, readline().split())
        E[u][v] = E[v][u] = d
    for i in range(N):
        E[i][i] = 0
    for k in range(N):
        for i in range(N):
            Ei = E[i]
            for j in range(N):
                Ei[j] = min(Ei[j], Ei[k] + E[k][j])
    g = HopcroftKarp(L, L)

    P = [list(map(int, readline().split())) for i in range(L)]
    P.sort(key = lambda x: x[1])
    for i in range(L):
        pi, ti = P[i]
        for j in range(i+1, L):
            pj, tj = P[j]
            if ti + E[pi][pj] <= tj:
                g.add_edge(i, j)
    write("%d\n" % (L - g.flow()))
    return True
while solve():
    ...
