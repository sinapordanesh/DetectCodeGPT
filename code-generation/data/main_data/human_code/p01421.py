# AOJ 2304 Reverse Roads
# Python3 2018.7.21 bal4u

# *******************************************
# Dinic's Max Flow Algorithm
# *******************************************
INF = 0x7fffffff

class Donic:
    def __init__(self, V):
        self.V = V
        self.level = [0] * V
        self.iter = [0] * V
        self.edge = [[] for i in range(V)]

    def add_edge(self, frm, to, cap):
        f, t = len(self.edge[frm]), len(self.edge[to])
        self.edge[frm].append([to, cap, t])
        self.edge[to].append([frm, cap, f])

    def bfs(self, s):
        self.level = [-1] * self.V
        self.level[s] = 0
        Q = []
        Q.append(s)
        while Q:
            v = Q.pop()
            for to, cap, rev in self.edge[v]:
                if cap > 0 and self.level[to] < 0:
                    self.level[to] = self.level[v] + 1
                    Q.append(to)

    def dfs(self, v, t, f):
        if v == t: return f
        k = self.iter[v]
        while k < len(self.edge[v]):
            to, cap, rev = self.edge[v][k]
            if cap > 0 and self.level[v] < self.level[to]:
                d = self.dfs(to, t, f if f <= cap else cap)
                if d > 0:
                    self.edge[v][k][1] -= d
                    self.edge[to][rev][1] += d
                    return d
            self.iter[v] += 1
            k += 1
        return 0

    def maxFlow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.level[t] < 0: break
            self.iter = [0] * self.V
            while True:
                f = self.dfs(s, t, INF)
                if f <= 0: break
                flow += f
        return flow

N, M = map(int, input().split())
dir = [[0 for j in range(N)] for i in range(N)]
id =  [[0 for j in range(N)] for i in range(N)]
d = Donic(N)
for i in range(M):
	x, y = map(int, input().split())
	x, y = x-1, y-1
	dir[y][x] = 1
	id[y][x] = i+1
	d.add_edge(x, y, 1)
S, T = map(int, input().split())
print(d.maxFlow(S-1, T-1))

ans = []
for i in range(N):
	for to, cap, rev in d.edge[i]:
		if cap < 1 and dir[i][to]: ans.append(id[i][to])
ans.sort()
print(len(ans))
if len(ans) > 0: print(*ans, sep='\n')

