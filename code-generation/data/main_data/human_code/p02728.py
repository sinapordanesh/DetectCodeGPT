class Tree():
    def __init__(self, n):
        self.n = n
        self.tree = [[] for _ in range(n)]
        self.root = None
        self.dep = [None] * n
        self.size = [1] * n

    def add_edges(self, e, idx=1):
        for u, v in e:
            self.tree[u - idx].append(v - idx)
            self.tree[v - udx].append(u - idx)

    def add_edge(self, u, v, idx=1):
        self.tree[u - idx].append(v - idx)
        self.tree[v - idx].append(u - idx)

    def set_root(self, r):
        self.root = r
        self.par = [None] * self.n
        self.par[r] = -1
        self.dep[r] = 0
        self.ord = [r]
        stack = [r]
        while stack:
            v = stack.pop()
            for adj in self.tree[v]:
                if self.par[adj] is not None: continue
                self.par[adj] = v
                self.dep[adj] = self.dep[v] + 1
                self.ord.append(adj)
                stack.append(adj)
        for v in self.ord[::-1]:
            for adj in self.tree[v]:
                if self.par[v] == adj: continue
                self.size[v] += self.size[adj]

    def diam(self):
        #assert self.root is not None
        u = self.dep.index(max(self.dep))
        dist = [None] * self.n
        dist[u] = 0
        prev = [None] * self.n
        stack = [u]
        while stack:
            v = stack.pop()
            for adj in self.tree[v]:
                if dist[adj] is not None: continue
                dist[adj] = dist[v] + 1
                prev[adj] = v
                stack.append(adj)
        d = max(dist)
        v = w = dist.index(d)
        path = [v]
        while w != u:
            w = prev[w]
            path.append(v)
        return d, v, u, path

    def rerooting(self, op, e, merge, id):
        #assert self.root is not None
        dp = [e] * self.n
        lt = [id] * self.n
        rt = [id] * self.n
        inv = [id] * self.n
        for v in self.ord[::-1]:
            tl = tr = e
            for adj in self.tree[v]:
                if self.par[v] == adj: continue
                lt[adj] = tl
                tl = op(tl, dp[adj])
            for adj in self.tree[v][::-1]:
                if self.par[v] == adj: continue
                rt[adj] = tr
                tr = op(tr, dp[adj])
            dp[v] = tr
        for v in self.ord:
            if v == self.root: continue
            p = self.par[v]
            inv[v] = op(merge(lt[v], rt[v]), inv[p])
            dp[v] = op(dp[v], inv[v])
        return dp

    def heavylight_decomposition(self):
        #assert self.root is not None
        self.vid = [None] * self.n
        self.head = [None] * self.n
        self.head[self.root] = self.root
        self.next = [None] * self.n
        stack = [self.root]
        cnt = 0
        while stack:
            v = stack.pop()
            self.vid[v] = cnt
            cnt += 1
            maxs = 0
            for adj in self.tree[v]:
                if self.par[v] == adj: continue
                if maxs < self.size[adj]:
                    maxs = self.size[adj]
                    self.next[v] = adj
            for adj in self.tree[v]:
                if self.par[v] == adj or self.next[v] == adj: continue
                self.head[adj] = adj
                stack.append(adj)
            if self.next[v] is not None:
                self.head[self.next[v]] = self.head[v]
                stack.append(self.next[v])

    def lca(self, u, v):
        while True:
            if self.vid[u] > self.vid[v]: u, v = v, u
            if self.head[u] != self.head[v]:
                v = self.par[self.head[v]]
            else:
                return u

    def range_query(self, u, v, edge_query=False):
        while True:
            if self.vid[u] > self.vid[v]: u, v = v, u
            if self.head[u] != self.head[v]:
                yield self.vid[self.head[v]], self.vid[v] + 1
                v = self.par[self.head[v]]
            else:
                yield self.vid[u] + edge_query, self.vid[v] + 1
                return

    def subtree_query(self, u):
        return self.vid[u], self.vid[u] + self.size[u]

def build_factorial(n):
    fct = [0] * (n + 1)
    ifct = [0] * (n + 1)
    fct[0] = ifct[0] = 1
    for i in range(n):
        fct[i + 1] = fct[i] * (i + 1) % MOD
    ifct[n] = pow(fct[n], MOD - 2, MOD)
    for i in range(n)[::-1]:
        ifct[i] = ifct[i + 1] * (i + 1) % MOD
    return fct, ifct

import sys
input = sys.stdin.buffer.readline

MOD = 1000000007

N = int(input())

fct, ifct = build_factorial(N + 1)
tree = Tree(N)

for _ in range(N - 1):
    u, v = map(int, input().split())
    tree.add_edge(u, v, 1)

tree.set_root(0)

def merge(lt, rt):
    lc, ls = lt
    rc, rs = rt
    size = ls + rs - 1
    cnt = lc * rc * ifct[ls - 1] * ifct[rs - 1] * fct[size - 1] % MOD
    return cnt, size

def op(v, ad):
    vc, vs = v
    adc, ads = ad
    size = vs + ads
    cnt = vc * adc * ifct[ads] * fct[size - 1] * ifct[vs - 1] % MOD
    return cnt, size

e = (1, 1)
id = (1, 0)

d = tree.rerooting(op, e, merge, id)
res = []

for cnt, size in d:
    res.append(cnt)

print('\n'.join(map(str, res)))