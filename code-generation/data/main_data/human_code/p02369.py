#!/usr/bin/env python3
# GRL_4_A: Path/Cycle - Cycle Detection for a Directed Graph


from collections import namedtuple

DirectedEdge = namedtuple('DirectedEdge', ('src', 'dest'))


class Digraph:
    def __init__(self, v):
        self.v = v
        self._edges = [[] for _ in range(v)]

    def add(self, edge):
        self._edges[edge.src].append(edge)

    def adj(self, v):
        return self._edges[v]

    def edges(self):
        for es in self._edges:
            for e in es:
                yield e


def has_cycle(graph):
    def dfs(v):
        if visited[v]:
            if not left[v]:
                return True
        else:
            visited[v] = True
            for e in graph.adj(v):
                if dfs(e.dest):
                    return True
            left[v] = True
        return False

    visited = [False] * graph.v
    left = [False] * graph.v

    for v in range(graph.v):
        if not visited[v] and dfs(v):
            return True

    return False


def run():
    v, e = [int(i) for i in input().split()]
    g = Digraph(v)

    for _ in range(e):
        s, t = [int(i) for i in input().split()]
        g.add(DirectedEdge(s, t))

    if has_cycle(g):
        print("1")
    else:
        print("0")


if __name__ == '__main__':
    run()

