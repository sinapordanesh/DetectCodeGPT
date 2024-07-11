#!/usr/bin/env python3
# GRL_5_B: Tree - Height of a Tree

import bisect


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


def heights(graph):
    def select_root():
        leaves = [v for v in range(graph.v) if len(graph.adj(v)) < 2]
        visited = [False] * graph.v
        while len(leaves) > 2:
            v, *leaves = leaves
            if not visited[v]:
                visited[v] = True
                for e in graph.adj(v):
                    w = e.other(v)
                    if not visited[w]:
                        visited[w] = True
                        leaves.append(w)
        return leaves.pop()

    def dfs(s):
        visited = [False] * graph.v
        stack = [s]
        while stack:
            v = stack.pop()
            if not visited[v]:
                visited[v] = True
                stack.append(v)
                for e in graph.adj(v):
                    w = e.other(v)
                    if not visited[w]:
                        edge_to[w] = e
                        stack.append(w)
            else:
                e = edge_to[v]
                if e is not None:
                    w = e.other(v)
                    bisect.insort(dists[w], (dists[v][-1][0] + e.weight, v))

    def _heights(s):
        hs = [0] * graph.v
        visited = [False] * graph.v
        stack = [s]
        while stack:
            v = stack.pop()
            if not visited[v]:
                visited[v] = True
                hs[v] = dists[v][-1][0]
                for e in graph.adj(v):
                    w = e.other(v)
                    if not visited[w]:
                        for x, xv in reversed(dists[v]):
                            if xv != w:
                                bisect.insort(dists[w], (x + e.weight, v))
                                break
                        stack.append(w)
        return hs

    root = select_root()
    edge_to = [None] * graph.v
    dists = [[(0, i)] for i in range(graph.v)]
    dfs(root)
    return _heights(root)


def run():
    n = int(input())
    g = Graph(n)

    for _ in range(n-1):
        s, t, w = [int(i) for i in input().split()]
        g.add(WeightedEdge(s, t, w))

    for w in heights(g):
        print(w)


if __name__ == '__main__':
    run()

