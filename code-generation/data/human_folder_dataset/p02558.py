import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


class DisjointSetUnion:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n
        self.rank = [0] * n

    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        self.par[y] = x
        return


if __name__ == '__main__':
    n, q = map(int, readline().split())
    dsu = DisjointSetUnion(n)

    for i in range(q):
        t, u, v = map(int, readline().split())

        if t:
            print(int(dsu.same(u, v)))
        else:
            dsu.unite(u, v)
