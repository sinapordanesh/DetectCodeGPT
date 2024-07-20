#!/usr/bin/env python3
# GRL_5_E: Tree - Range Query on Tree 2


# Undirected Graph
class Edge:
    __slots__ = ('v', 'w')

    def __init__(self, v, w):
        self.v = v
        self.w = w

    def either(self):
        return self.v

    def other(self, v):
        if v == self.v:
            return self.w
        else:
            return self.v


class Graph:
    def __init__(self, v):
        self.v = v
        self._edges = [[] for _ in range(v)]

    def add(self, e):
        self._edges[e.v].append(e)
        self._edges[e.w].append(e)

    def adj(self, v):
        return self._edges[v]

    def edges(self):
        for es in self._edges:
            for e in es:
                yield e


class HeavyLightDecomposition:
    class _Path:
        __slots__ = ('nodes', '_index')

        def __init__(self):
            self.nodes = []
            self._index = None

        @property
        def head(self):
            return self.nodes[0]

        @property
        def size(self):
            return len(self.nodes)

        def append(self, v):
            self.nodes.append(v)

        def index(self, v):
            if self._index is None:
                self._index = {v: i for i, v in enumerate(self.nodes)}
            return self._index[v]

        def next(self, v):
            return self.nodes[self.index(v)+1]

    def __init__(self, graph, root):
        self._paths = {}
        self._parent = [root] * graph.v
        self._head = [-1] * graph.v
        self._find_paths(graph, root)

    def _find_paths(self, graph, root):
        def create_path(v):
            path = self._Path()
            u = v
            while u != -1:
                path.append(u)
                self._head[u] = v
                u = heavy[u]
            return path

        size = [1] * graph.v
        maxsize = [0] * graph.v
        heavy = [-1] * graph.v
        visited = [False] * graph.v

        stack = [root]
        while stack:
            v = stack.pop()
            if not visited[v]:
                visited[v] = True
                stack.append(v)
                for e in graph.adj(v):
                    w = e.other(v)
                    if not visited[w]:
                        self._parent[w] = v
                        stack.append(w)
            else:
                if v != root:
                    p = self._parent[v]
                    if size[v] > maxsize[p]:
                        maxsize[p] = size[v]
                        heavy[p] = v
                    size[p] += size[v]
                for e in graph.adj(v):
                    w = e.other(v)
                    if w != self._parent[v] and w != heavy[v]:
                        self._paths[w] = create_path(w)

        self._paths[root] = create_path(root)

    def parent(self, v):
        return self._parent[v]

    def paths(self):
        return self._paths.values()

    def get_path(self, v):
        return self._paths[self._head[v]]


class PathSum2:
    """PathSum with range update.
    """
    def __init__(self, graph, root):
        self.root = root
        self.hld = HeavyLightDecomposition(graph, root)
        self.rq = {p.head: RangeQuery(p.size) for p in self.hld.paths()}

    def add(self, v, val):
        u = v
        while u != self.root:
            path = self.hld.get_path(u)
            head = path.head
            if head != self.root:
                i = path.index(head)
            else:
                i = path.index(path.next(head))
            j = path.index(u)
            self.rq[head].add(i+1, j+1, val)
            u = self.hld.parent(head)

    def get(self, v):
        weight = 0
        u = v
        while u != self.root:
            path = self.hld.get_path(u)
            head = path.head
            i = path.index(head)
            j = path.index(u)
            weight += self.rq[head].sum(i+1, j+1)
            u = self.hld.parent(head)

        return weight


# Binary Indexed Tree
class BinaryIndexedTree:
    def __init__(self, n):
        self.size = n
        self.bit = [0] * (self.size+1)

    def add(self, i, v):
        while i <= self.size:
            self.bit[i] += v
            i += (i & -i)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= (i & -i)
        return s


class RangeQuery:
    def __init__(self, n):
        self.size = n
        self.bit1 = BinaryIndexedTree(n+1)
        self.bit2 = BinaryIndexedTree(n+1)

    def add(self, i, j, v):
        self.bit1.add(i, v * -i)
        self.bit1.add(j+1, v * (j+1))
        self.bit2.add(i, v)
        self.bit2.add(j+1, -v)

    def sum(self, i, j):
        s = self.bit1.sum(j+1) + (j+1)*self.bit2.sum(j+1)
        s -= self.bit1.sum(i) + i*self.bit2.sum(i)
        return s


def run():
    n = int(input())
    g = Graph(n)

    for i in range(n):
        k, *cs = [int(i) for i in input().split()]
        if k > 0:
            for j in cs:
                g.add(Edge(i, j))

    ps = PathSum2(g, 0)
    q = int(input())
    for _ in range(q):
        com, *args = [int(i) for i in input().split()]
        if com == 0:
            u, val = args
            ps.add(u, val)
        elif com == 1:
            u, = args
            print(ps.get(u))
        else:
            raise ValueError('invalid command')


if __name__ == '__main__':
    run()

