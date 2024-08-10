import collections


def plus_list(A, B):
    assert(len(A) == len(B))
    return [a + b for a, b in zip(A, B)]


def minus_list(A, B):
    assert(len(A) == len(B))
    return [a - b for a, b in zip(A, B)]


def gt_list(A, B):
    assert(len(A) == len(B))
    for a, b in zip(A, B):
        if a != b:
            return a > b
    return False


class MaxFlow:
    """Dinic Algorithm: find max-flow
       complexity: O(EV^2)
       used in GRL6A(AOJ)
    """
    class Edge:
        def __init__(self, to, cap, rev):
            self.to, self.cap, self.rev = to, cap, rev

    def __init__(self, V, D):
        """ V: the number of vertexes
            E: adjacency list
            source: start point
            sink: goal point
        """
        self.V = V
        self.E = [[] for _ in range(V)]
        self.D = D

    def add_edge(self, fr, to, cap):
        self.E[fr].append(self.Edge(to, cap, len(self.E[to])))
        self.E[to].append(self.Edge(fr, [0] * self.D, len(self.E[fr])-1))

    def dinic(self, source, sink):
        """find max-flow"""
        INF = [10**9] * self.D
        maxflow = [0] * self.D
        while True:
            self.bfs(source)
            if self.level[sink] < 0:
                return maxflow
            self.itr = [0] * self.V
            while True:
                flow = self.dfs(source, sink, INF)
                if gt_list(flow, [0] * self.D):
                    maxflow = plus_list(maxflow, flow)
                else:
                    break

    def dfs(self, vertex, sink, flow):
        """find augmenting path"""
        if vertex == sink:
            return flow
        for i in range(self.itr[vertex], len(self.E[vertex])):
            self.itr[vertex] = i
            e = self.E[vertex][i]
            if gt_list(e.cap, [0] * self.D) and self.level[vertex] < self.level[e.to]:
                if gt_list(flow, e.cap):
                    d = self.dfs(e.to, sink, e.cap)
                else:
                    d = self.dfs(e.to, sink, flow)
                if gt_list(d, [0] * self.D):
                    e.cap = minus_list(e.cap, d)
                    self.E[e.to][e.rev].cap = plus_list(self.E[e.to][e.rev].cap, d)
                    return d
        return [0] * self.D

    def bfs(self, start):
        """find shortest path from start"""
        que = collections.deque()
        self.level = [-1] * self.V
        que.append(start)
        self.level[start] = 0

        while que:
            fr = que.popleft()
            for e in self.E[fr]:
                if gt_list(e.cap, [0] * self.D) and self.level[e.to] < 0:
                    self.level[e.to] = self.level[fr] + 1
                    que.append(e.to)


def to_poly(a, l):
    if l == 0:
        return str(a)
    elif l == 1:
        return "{}x".format('' if a == 1 else a)
    else:
        return "{}x^{}".format('' if a == 1 else a, l)

while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    mf = MaxFlow(N, 51)
    for _ in range(M):
        u, v, p = input().split()
        u, v = int(u)-1, int(v)-1
        poly = [0] * 51
        for x in p.split('+'):
            try:
                num = int(x)
                poly[-1] = num
            except ValueError:
                a, l = x.split('x')
                if l:
                    poly[-int(l.strip("^"))-1] = int(a) if a else 1
                else:
                    poly[-2] = int(a) if a else 1
        mf.add_edge(u, v, poly)
        mf.add_edge(v, u, poly)
    maxflow = mf.dinic(0, N-1)
    ans = '+'.join(to_poly(a, l) for a, l in zip(maxflow, reversed(range(51))) if a)
    print(ans if ans else 0)