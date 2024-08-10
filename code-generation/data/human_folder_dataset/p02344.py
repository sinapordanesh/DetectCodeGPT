#!/usr/bin/env python3
# DSL_1_B: Weighted Union Find Trees


class WeightedUnionFind:
    def __init__(self, n):
        self.n = n
        self.nodes = [i for i in range(n)]
        self.weights = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def connected(self, i, j):
        wi, ri = self.root(i)
        wj, rj = self.root(j)
        return ri == rj

    def union(self, i, j, w):
        wi, ri = self.root(i)
        wj, rj = self.root(j)
        if ri == rj:
            return

        if self.size[ri] < self.size[rj]:
            self.nodes[ri] = rj
            self.weights[ri] = wj - wi + w
            self.size[rj] += self.size[ri]
        else:
            self.nodes[rj] = ri
            self.weights[rj] = wi - wj - w
            self.size[ri] += self.size[rj]

    def weight(self, i, j):
        wi, ri = self.root(i)
        wj, rj = self.root(j)
        if ri != rj:
            raise ValueError('{} and {} is not connected'.format(i, j))

        return wi - wj

    def root(self, i):
        r = self.nodes[i]
        w = self.weights[i]
        while r != self.nodes[r]:
            w += self.weights[r]
            r = self.nodes[r]
        return w, r


def run():
    n, q = [int(i) for i in input().split()]
    wuf = WeightedUnionFind(n)

    for _ in range(q):
        com, *args = input().split()
        if com == '0':
            wuf.union(*[int(i) for i in args])
        elif com == '1':
            x, y = [int(i) for i in args]
            if wuf.connected(x, y):
                print(wuf.weight(x, y))
            else:
                print('?')


if __name__ == '__main__':
    run()

