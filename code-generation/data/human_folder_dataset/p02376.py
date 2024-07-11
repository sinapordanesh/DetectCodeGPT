INF = 10**12
N = 101


class FordFulkerson:
    def __init__(self):
        self.G = [[] for _ in range(N)]
        self.used = [False] * N

    def add_edge(self, s, t, c):
        self.G[s].append([t, c, len(self.G[t])])
        self.G[t].append([s, 0, len(self.G[s])-1])

    def dfs(self, s, t, f):
        if s == t:
            return f
        self.used[s] = True
        for i in range(len(self.G[s])):
            e = self.G[s][i]
            if not self.used[e[0]] and e[1] > 0:
                d = self.dfs(e[0], t, min(f, e[1]))
                if d > 0:
                    self.G[s][i][1] -= d
                    self.G[e[0]][e[2]][1] += d
                    return d
        return 0

    def max_flow(self, s, t):
        flow = 0
        while True:
            self.used = [False]*N
            f = self.dfs(s, t, INF)
            if f == 0:
                return flow
            flow += f

if __name__ == "__main__":
    V, E = map(int, input().split())
    ff = FordFulkerson()
    for i in range(E):
        u, v, c = map(int, input().split())
        ff.add_edge(u, v, c)
    print(ff.max_flow(0, V-1))


