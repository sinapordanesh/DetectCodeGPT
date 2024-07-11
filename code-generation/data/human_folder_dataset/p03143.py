import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, N):
        self.par = [-1] * N

    def find(self, x):
        r = x
        while self.par[r] >= 0:
            r = self.par[r]
        while x != r:
            tmp = self.par[x]
            self.par[x] = r
            x = tmp
        return r

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.par[x] > self.par[y]:
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.par[self.find(x)]

N, M = map(int, input().split())
X = list(map(int, input().split()))
G = [[] for _ in range(N)]
edges = []
for _ in range(M):
    A, B, Y = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)
    edges.append((A, B, Y))
edges.sort(key=lambda p: p[2])
use = 0
pending = [0] * N
uf = UnionFind(N)
for A, B, Y in edges:
    s = X[uf.find(A)]
    if not uf.same(A, B):
        s += X[uf.find(B)]
        t = pending[uf.find(A)] + pending[uf.find(B)]
        uf.unite(A, B)
        X[uf.find(A)] = s
        pending[uf.find(A)] = t
    if Y <= s:
        use += pending[uf.find(A)] + 1
        pending[uf.find(A)] = 0
    else:
        pending[uf.find(A)] += 1
print(M - use)