import sys
readline = sys.stdin.readline
write = sys.stdout.write

from collections import deque
class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]
        self.D = {}

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)
        self.D[fr, to] = forward

    def bfs(self, s, t):
        self.level = level = [None]*self.N
        deq = deque([s])
        level[s] = 0
        G = self.G
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10**9 + 7
        G = self.G
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow

def solve():
    N, M, S, T = map(int, readline().split())
    if N == M == 0:
        return False
    S -= 1; T -= 1
    E = []
    INF = 10**9
    dinic = Dinic(N)
    for i in range(M):
        a, b = map(int, readline().split()); a -= 1; b -= 1
        dinic.add_edge(a, b, 1)
        E.append((a, b))
    f = dinic.flow(S, T)

    used = [0]*N
    que = deque([S])
    used[S] = 1
    while que:
        v = que.popleft()
        for w, cap, _ in dinic.G[v]:
            if cap == 0 or used[w]:
                continue
            used[w] = 1
            que.append(w)
    que = deque([T])
    used[T] = 2
    while que:
        v = que.popleft()
        for w, cap, _ in dinic.G[v]:
            if cap > 0 or used[w]:
                continue
            used[w] = 2
            que.append(w)
    cnt = 0
    for a, b in E:
        if used[a] == 2 and used[b] == 1:
            cnt += 1
    if cnt:
        write("%d %d\n" % (f+1, cnt))
    else:
        write("%d %d\n" % (f, 0))
    return True
while solve():
    ...
