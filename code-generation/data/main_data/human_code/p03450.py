class WeightedUnionFind:
    def __init__(self, n):
        self.n = n
        self.par = list(range(n))
        self.rank = [0] * n
        self.weight = [0] * n
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y
    def unite(self, x, y, w):
        p, q = self.find(x), self.find(y)
        if self.rank[p] < self.rank[q]:
            self.par[p] = q
            self.weight[p] = w - self.weight[x] + self.weight[y]
        else:
            self.par[q] = p
            self.weight[q] = -w - self.weight[y] + self.weight[x]
            if self.rank[p] == self.rank[q]:
                self.rank[p] += 1
    def same(self, x, y):
        return self.find(x) == self.find(y)
    def diff(self, x, y):
        return self.weight[x] - self.weight[y]
n, m = map(int, input().split())
UF = WeightedUnionFind(n)
for i in range(m):
    l, r, d = map(int, input().split())
    if UF.same(l - 1, r - 1):
        if UF.diff(l - 1, r - 1) != d:
            exit(print("No"))
    else:
        UF.unite(l - 1, r - 1, d)
print("Yes")