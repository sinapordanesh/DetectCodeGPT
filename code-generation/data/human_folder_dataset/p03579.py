from collections import deque


class Graph:
    def __init__(self, n):
        self.n = n
        self.edge = [[] for _ in range(n)]
        self.color = [-1] * n

    def add_edge(self, node1, node2):
        self.edge[node1].append(node2)
        self.edge[node2].append(node1)

    def is_bipartite_graph(self):
        self.color = [-1] * self.n

        for i in range(self.n):
            if self.color[i] == -1:
                self.color[i] = 0
                d = deque([(i, 0)])

                while d:
                    node, c = d.pop()
                    for j in self.edge[node]:
                        if self.color[j] == -1:
                            self.color[j] = c ^ 1
                            d.append((j, self.color[j]))
                        elif self.color[j] == c:
                            return False

        return True


N, M = map(int, input().split())

g = Graph(N)

for i in range(M):
    A, B = map(int, input().split())
    g.add_edge(A-1, B-1)

if g.is_bipartite_graph():
    zero = g.color.count(0)
    print(zero * (N - zero) - M)
else:
    print(N * (N - 1) // 2 - M)
