class Tree():
    def __init__(self, n, decrement=1):
        self.n = n
        self.edges = [[] for _ in range(n)]
        self.root = None
        self.depth = [-1]*n
        self.size = [1]*n       # 部分木のノードの数
        self.decrement = decrement

    def add_edge(self, u, v):
        u, v = u-self.decrement, v-self.decrement
        self.edges[u].append(v)
        self.edges[v].append(u)

    def add_edges(self, edges):
        for u, v in edges:
            u, v = u-self.decrement, v-self.decrement
            self.edges[u].append(v)
            self.edges[v].append(u)

    def set_root(self, root):
        root -= self.decrement
        self.root = root
        self.par = [-1]*self.n
        self.depth[root] = 0
        self.order = [root]     # 帰りがけに使う
        next_set = [root]
        while next_set:
            p = next_set.pop()
            for q in self.edges[p]:
                if self.depth[q] != -1: continue
                self.par[q] = p
                self.depth[q] = self.depth[p]+1
                self.order.append(q)
                next_set.append(q)
        for p in self.order[::-1]:
            for q in self.edges[p]:
                if self.par[p] == q: continue
                self.size[p] += self.size[q]


#########################################################################################################
import sys
input = sys.stdin.readline

N = int(input())
T = Tree(N, decrement=1)
for _ in range(N-1):
    x, y = map(int, input().split())
    T.add_edge(x, y)
T.set_root(1)

grundy = [0]*N
for p in T.order[::-1]:
    for q in T.edges[p]:
        if T.par[p]==q: continue
        grundy[p]^=grundy[q]+1

print("Alice" if grundy[0]!=0 else "Bob")