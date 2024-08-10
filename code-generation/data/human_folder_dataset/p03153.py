def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline

    class UnionFind():
        def __init__(self, n):
            self.n = n
            self.root = [-1] * (n + 1)
            self.rnk = [0] * (n + 1)

        def find_root(self, x):
            if self.root[x] < 0:
                return x
            else:
                self.root[x] = self.find_root(self.root[x])
                return self.root[x]

        def unite(self, x, y):
            x = self.find_root(x)
            y = self.find_root(y)
            if x == y:
                return
            elif self.rnk[x] > self.rnk[y]:
                self.root[x] += self.root[y]
                self.root[y] = x
            else:
                self.root[y] += self.root[x]
                self.root[x] = y
                if self.rnk[x] == self.rnk[y]:
                    self.rnk[y] += 1

        def isSameGroup(self, x, y):
            return self.find_root(x) == self.find_root(y)

        def size(self, x):
            return -self.root[self.find_root(x)]

    class Bit:
        def __init__(self, n):
            self.size = n
            self.inf = 10 ** 15
            self.tree = [self.inf] * (n + 1)

        def query(self, i):
            s = self.inf
            while i > 0:
                s = min(self.tree[i], s)
                i -= i & -i
            return s

        def update(self, i, x):
            while i <= self.size:
                self.tree[i] = min(self.tree[i], x)
                i += i & -i

    N, D = map(int, input().split())
    A = list(map(int, input().split()))

    tmp = [(a, i+1) for i, a in enumerate(A)]
    tmp.sort(key=lambda x: x[0])
    segtree_plus = Bit(N+5)
    segtree_minus = Bit(N+5)
    edge = []
    val2idx_plus = defaultdict(int)
    val2idx_minus = defaultdict(lambda: N+3)
    edge_append = edge.append
    inf = 10**15
    for a, i in tmp:
        val_plus = a+D*i
        val_minus = a-D*i
        segtree_plus.update(N+1-i, val_plus)
        segtree_minus.update(i, val_minus)
        i_ori = val2idx_plus[val_plus]
        if i > i_ori:
            val2idx_plus[val_plus] = i
        i_ori = val2idx_minus[val_minus]
        if i < i_ori:
            val2idx_minus[val_minus] = i
        plus_min = segtree_plus.query(N-i)
        if plus_min < inf:
            j_plus = val2idx_plus[plus_min]
            edge_append((i, j_plus, A[i-1] + A[j_plus-1] + D*(j_plus - i)))
        minus_min = segtree_minus.query(i-1)
        if minus_min < inf:
            j_minus = val2idx_minus[minus_min]
            edge_append((i, j_minus, A[i-1] + A[j_minus-1] + D * (i - j_minus)))

    edge.sort(key=lambda x: x[2])
    UF = UnionFind(N + 1)
    ans = 0
    for u, v, cost in edge:
        if UF.isSameGroup(u, v):
            continue
        ans += cost
        UF.unite(u, v)
    print(ans)


if __name__ == '__main__':
    main()
