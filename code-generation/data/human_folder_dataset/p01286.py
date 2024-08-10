import collections


class MaxFlow:
    """Dinic Algorithm: find max-flow
       complexity: O(EV^2)
       used in GRL6A(AOJ)
    """
    class Edge:
        def __init__(self, to, cap, rev):
            self.to, self.cap, self.rev = to, cap, rev

    def __init__(self, V):
        """ V: the number of vertexes
            E: adjacency list
            source: start point
            sink: goal point
        """
        self.V = V
        self.E = [[] for _ in range(V)]

    def add_edge(self, fr, to, cap):
        self.E[fr].append(self.Edge(to, cap, len(self.E[to])))
        self.E[to].append(self.Edge(fr, 0, len(self.E[fr])-1))

    def run(self, source, sink, INF=10**9):
        """find max-flow"""
        maxflow = 0
        while True:
            self.bfs(source)
            if self.level[sink] < 0:
                return maxflow
            self.itr = [0] * self.V
            while True:
                flow = self.dfs(source, sink, INF)
                if flow > 0:
                    maxflow += flow
                else:
                    break

    def dfs(self, vertex, sink, flow):
        """find augmenting path"""
        if vertex == sink:
            return flow
        for i in range(self.itr[vertex], len(self.E[vertex])):
            self.itr[vertex] = i
            e = self.E[vertex][i]
            if e.cap > 0 and self.level[vertex] < self.level[e.to]:
                d = self.dfs(e.to, sink, min(flow, e.cap))
                if d > 0:
                    e.cap -= d
                    self.E[e.to][e.rev].cap += d
                    return d
        return 0

    def bfs(self, start):
        """find shortest path from start"""
        que = collections.deque()
        self.level = [-1] * self.V
        que.append(start)
        self.level[start] = 0

        while que:
            fr = que.popleft()
            for e in self.E[fr]:
                if e.cap > 0 and self.level[e.to] < 0:
                    self.level[e.to] = self.level[fr] + 1
                    que.append(e.to)

while True:
    H, W, C, M, NW, NC, NM = map(int, input().split())
    if H == -1:
        break
    V = H + 2 * (W + C) + M + 5 + 2
    mf = MaxFlow(V)
    source, sink = V - 2, V - 1

    inH = lambda i: i
    inW = lambda i: H + i
    outW = lambda i: H + W + i
    inC = lambda i: H + 2 * W + i
    outC = lambda i: H + 2 * W + C + i
    inM = lambda i: H + 2 * (W + C) + i
    inNW = H + 2 * (W + C) + M
    outNW = inNW + 1
    inNC = outNW + 1
    outNC = inNC + 1
    inNM = outNC + 1

    # source -> H
    for i in range(H):
        mf.add_edge(source, inH(i), 1)

    # H -> inW
    for i in range(W):
        friends = [int(x) - 1 for x in input().split()][1:]
        for friend in friends:
            mf.add_edge(inH(friend), inW(i), 1)

    # H -> inNW
    for i in range(H):
        mf.add_edge(inH(i), inNW, 1)

    # inW -> outW, inNW -> outNW
    for i in range(W):
        mf.add_edge(inW(i), outW(i), 1)
    mf.add_edge(inNW, outNW, NW)

    # outW -> inC, outNW -> inC
    for i in range(C):
        friends = [int(x) - 1 for x in input().split()][1:]
        for friend in friends:
            mf.add_edge(outW(friend), inC(i), 1)
        mf.add_edge(outNW, inC(i), 1)

    # outW -> inNC
    for i in range(W):
        mf.add_edge(outW(i), inNC, 1)

    # inC -> outC, inNC -> outNC
    for i in range(C):
        mf.add_edge(inC(i), outC(i), 1)
    mf.add_edge(inNC, outNC, NC)

    # outC -> M, outNC -> M
    for i in range(M):
        friends = [int(x) - 1 for x in input().split()][1:]
        for friend in friends:
            mf.add_edge(outC(friend), inM(i), 1)
        mf.add_edge(outNC, inM(i), 1)

    # outC -> NM
    for i in range(C):
        mf.add_edge(outC(i), inNM, 1)

    # M -> sink, NM -> sink
    for i in range(M):
        mf.add_edge(inM(i), sink, 1)
    mf.add_edge(inNM, sink, NM)

    print(mf.run(source, sink))