import heapq


class Edge:
    def __init__(self, dst, weight, cost):
        self.dst, self.weight, self.cost = dst, weight, cost

    def __lt__(self, e):
        return self.weight > e.weight


class Graph:
    def __init__(self, V):
        self.V = V
        self.E = [[] for _ in range(V)]

    def add_edge(self, src, dst, weight, cost):
        self.E[src].append(Edge(dst, weight, cost))


class ShortestPath:
    """Dijkstra's algorithm : find the shortest path from a vertex
       Complexity: O(E + log(V))
       used in GRL1A(AOJ)
    """

    def __init__(self, G, INF=10**9):
        """ V: the number of vertexes
            E: adjacency list (all edge in E must be 0 or positive)
            start: start vertex
            INF: Infinity distance
        """
        self.G, self.INF = G, INF

    class Node:
        def __init__(self, v, cost):
            self.v, self.cost = v, cost

        def __lt__(self, n):
            return self.cost < n.cost

    def dijkstra(self, start, goal=None):
        que = list()
        self.dist = [self.INF] * self.G.V  # distance from start
        self.prev = [-1] * self.G.V  # prev vertex of shortest path
        self.dist[start] = 0
        heapq.heappush(que, self.Node(start, 0))

        while len(que) > 0:
            n = heapq.heappop(que)
            if self.dist[n.v] < n.cost:
                continue
            if goal is not None and n.v == goal:
                return
            for e in self.G.E[n.v]:
                if self.dist[n.v] + e.weight < self.dist[e.dst]:
                    self.dist[e.dst] = self.dist[n.v] + e.weight
                    heapq.heappush(que, self.Node(e.dst, self.dist[e.dst]))
                    self.prev[e.dst] = n.v

    def getPath(self, end):
        path = [end]
        while self.prev[end] != -1:
            end = self.prev[end]
        return path[::-1]


while True:
    N, M = map(int, input().split())
    if not (N | M):
        break
    g = Graph(N)
    for _ in range(M):
        u, v, d, c = map(int, input().split())
        g.add_edge(u - 1, v - 1, d, c)
        g.add_edge(v - 1, u - 1, d, c)
    sp = ShortestPath(g)
    sp.dijkstra(0)
    print(sum(min(e.cost for e in g.E[i] if sp.dist[e.dst] + e.weight == sp.dist[i]) for i in range(1, N)))