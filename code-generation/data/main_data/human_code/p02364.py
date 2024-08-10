import sys


class UnionFind:
    def __init__(self, node_size):
        self._node = node_size
        self.par = [i for i in range(self._node)]
        self.rank = [0] * self._node

    def find(self, ver):
        if self.par[ver] == ver:
            return ver
        else:
            self.par[ver] = self.find(self.par[ver])
            return self.par[ver]

    def unite(self, ver1, ver2):
        ver1, ver2 = self.find(ver1), self.find(ver2)
        if ver1 == ver2:
            return
        if self.rank[ver1] < self.rank[ver2]:
            ver1, ver2 = ver2, ver1
        self.par[ver2] = ver1
        if self.rank[ver1] == self.rank[ver2]:
            self.rank[ver1] += 1

    def same(self, ver1, ver2):
        return self.find(ver1) == self.find(ver2)


class Kruskal:

    class Edge:
        def __init__(self, u, v, cost):
            self.u, self.v, self.cost = u, v, cost

        def __lt__(self, another):
            return self.cost < another.cost

    def __init__(self, node_size):
        self._node = node_size
        self._edge_list = []

    def add_edge(self, u, v, cost):
        self._edge_list.append(self.Edge(u, v, cost))

    def solve(self):
        uf = UnionFind(self._node)
        res = 0
        edge_count = 0
        sorted_edge_list = sorted(self._edge_list)
        for e in sorted_edge_list:
            if not uf.same(e.u, e.v):
                uf.unite(e.u, e.v)
                res += e.cost
                edge_count += 1
                if edge_count == self._node-1:
                    break
        return res

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    kr = Kruskal(n)
    for _ in range(m):
        s, t, w = map(int, sys.stdin.readline().split())
        kr.add_edge(s, t, w)
    print(kr.solve())

