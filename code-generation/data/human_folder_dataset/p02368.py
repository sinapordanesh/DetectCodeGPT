#!/usr/bin/env python3
# GRL_3_C: Connected Components - Strongly Connected Components


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


def scc_kosaraju_sharir(graph):
    class CC:
        def __init__(self, v):
            self._id = [i for i in range(v)]

        def id(self, v, c):
            self._id[v] = c

        def connected(self, u, v):
            return self._id[u] == self._id[v]

    def dfs(v):
        stack = [v]
        while stack:
            w = stack.pop()
            if not visited[w]:
                visited[w] = True
                yield w
                stack.extend([e.dest for e in graph.adj(w)
                              if not visited[e.dest]])

    visited = [False] * graph.v
    i = 0
    cc = CC(graph.v)
    for v in reverse_post(graph.reversed()):
        if not visited[v]:
            for w in dfs(v):
                cc.id(w, i)
            i += 1
    return cc


def run():
    v, e = [int(i) for i in input().split()]
    g = Digraph(v)

    for _ in range(e):
        s, t = [int(i) for i in input().split()]
        g.add(DirectedEdge(s, t))

    cc = scc_kosaraju_sharir(g)
    q = int(input())
    for _ in range(q):
        u, w = [int(i) for i in input().split()]
        if cc.connected(u, w):
            print(1)
        else:
            print(0)


if __name__ == '__main__':
    run()

