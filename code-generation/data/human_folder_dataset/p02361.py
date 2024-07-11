import sys
import heapq as hp

class Edge:
    def __init__(self, end, cost):
        self.to = end
        self.cost = cost


class Dijkstra:
    def __init__(self, V):
        self._node = V
        self._graph = [[] for i in range(self._node)]
        self._inf = sys.maxsize
        self.dist = [self._inf for i in range(self._node)]

    def add_edge(self, st, ed, cost):
        self._graph[st].append(Edge(ed, cost))
    def solve(self, s):
        que = []
        self.dist[s] = 0
        hp.heappush(que, (0, s))
        while que:
            cur_cost, cur_vertex = hp.heappop(que)
            if self.dist[cur_vertex] < cur_cost:
                continue
            for e in self._graph[cur_vertex]:
                if cur_cost + e.cost < self.dist[e.to]:
                    self.dist[e.to] = cur_cost + e.cost
                    hp.heappush(que, (self.dist[e.to], e.to))


if __name__ == '__main__':
    V, E, r = map(int, input().split())
    dk = Dijkstra(V)
    for i in range(E):
        s, t, d = map(int, input().split())
        dk.add_edge(s, t, d)
    dk.solve(r)
    for value in dk.dist:
        if value == sys.maxsize:
            print("INF")
        else:
            print(value)

