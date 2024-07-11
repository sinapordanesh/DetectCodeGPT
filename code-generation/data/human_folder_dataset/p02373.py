#!/usr/bin/env python3
# GRL_5_C: Tree - Lowest Common Ancestor


class UnionFind:
    def __init__(self, n):
        self.nodes = [i for i in range(n)]
        self.sizes = [1 for _ in range(n)]

    def union(self, p, q):
        rp = self.root(p)
        rq = self.root(q)
        if self.sizes[rp] > self.sizes[rq]:
            self.nodes[rq] = rp
            self.sizes[rp] += self.sizes[rq]
        else:
            self.nodes[rp] = rq
            self.sizes[rq] += self.sizes[rp]

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def root(self, p):
        while p != self.nodes[p]:
            self.nodes[p] = self.nodes[self.nodes[p]]
            p = self.nodes[p]

        return p


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


class WeightedEdge(Edge):
    __slots__ = ('v', 'w', 'weight')

    def __init__(self, v, w, weight):
        super().__init__(v, w)
        self.weight = weight


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


def lca(graph, root, queries):
    index = [set() for _ in range(graph.v)]
    for v, w in queries:
        index[v].add((v, w))

    visited = [False] * graph.v
    stored = [False] * graph.v
    parents = [None] * graph.v
    uf = UnionFind(graph.v)
    res = {}
    stack = [root]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            stack.append(v)
            for e in graph.adj(v):
                w = e.other(v)
                if not visited[w]:
                    stack.append(w)
                    parents[w] = v
        else:
            stored[v] = True
            p = parents[v]
            rest = set()
            for i, j in index[v]:
                if stored[i] and stored[j]:
                    if uf.connected(i, j) and (i, j) not in res:
                        res[(i, j)] = v
                    else:
                        rest.add((i, j))
                else:
                    index[j].add((i, j))
            index[v] = None
            if p is not None:
                uf.union(p, v)
                index[p].update(rest)

    return res


def run():
    n = int(input())
    g = Graph(n)

    for i in range(n):
        k, *cs = [int(i) for i in input().split()]
        if k > 0:
            for j in cs:
                g.add(Edge(i, j))

    q = int(input())
    qs = []
    for _ in range(q):
        v, w = [int(i) for i in input().split()]
        qs.append((v, w))

    res = lca(g, 0, qs)
    for v, w in qs:
        print(res[(v, w)])


if __name__ == '__main__':
    run()

