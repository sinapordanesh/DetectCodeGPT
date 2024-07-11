
class UF:
    """Union Find
    """
    def __init__(self, n):
        self.n = n
        self.elements = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def union(self, v, w):
        assert 0 <= v < self.n
        assert 0 <= w < self.n
        rv = self.root(v)
        rw = self.root(w)

        if rv != rw:
            if self.size[rv] > self.size[rw]:
                self.elements[rw] = rv
                self.size[rv] += self.size[rw]
            else:
                self.elements[rv] = rw
                self.size[rw] += self.size[rv]

    def connected(self, v, w):
        assert 0 <= v < self.n
        assert 0 <= w < self.n
        return self.root(v) == self.root(w)

    def root(self, v):
        rv = self.elements[v]
        while rv != self.elements[rv]:
            rv = self.elements[rv]
        return rv


def run():
    n, q = [int(x) for x in input().split()]
    uf = UF(n)

    for _ in range(q):
        com, i, j = [int(x) for x in input().split()]
        if com == 0:
            uf.union(i, j)
        elif com == 1:
            if uf.connected(i, j):
                print(1)
            else:
                print(0)


if __name__ == '__main__':
    run()

