#!/usr/bin/env python3
# GRL_4_B: Path/Cycle - Topological Sort

from collections import namedtuple


DirectedEdge = namedtuple('DirectedEdge', ('src', 'dest'))


def revert(edge):
    return edge._replace(src=edge.dest, dest=edge.src)


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

    def reversed(self):
        g = self.__class__(self.v)
        for e in self.edges():
            g.add(revert(e))

        return g


def sorted_topological(graph):
    return reversed(list(reverse_post(graph.reversed())))


def reverse_post(graph):
    def visit(v):
        if not visited[v]:
            visited[v] = True
            return True
        else:
            return False

    def leave(v):
        if not left[v]:
            left[v] = True
            vs.append(v)
        return False

    visited = [False] * graph.v
    left = [False] * graph.v
    vs = []

    for i in range(graph.v):
        if not visited[i]:
            stack = [(i, leave)]
            stack.extend((e.dest, visit) for e in graph.adj(i))
            while stack:
                v, f = stack.pop()
                if f(v):
                    stack.append((v, leave))
                    for e in graph.adj(v):
                        stack.append((e.dest, visit))
    return reversed(vs)


def run():
    v, e = [int(i) for i in input().split()]
    g = Digraph(v)

    for _ in range(e):
        s, t = [int(i) for i in input().split()]
        g.add(DirectedEdge(s, t))

    for v in sorted_topological(g):
        print(v)


if __name__ == '__main__':
    run()

