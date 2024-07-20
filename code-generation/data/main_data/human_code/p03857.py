from collections import Counter
import sys


class UnionFind:
    def __init__(self, n):
        self.table = [-1] * n

    def _root(self, x):
        stack = []
        tbl = self.table
        while tbl[x] >= 0:
            stack.append(x)
            x = tbl[x]
        for y in stack:
            tbl[y] = x
        return x

    def find(self, x, y):
        return self._root(x) == self._root(y)

    def union(self, x, y):
        r1 = self._root(x)
        r2 = self._root(y)
        if r1 == r2:
            return
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1 <= d2:
            self.table[r2] = r1
            self.table[r1] += d2
        else:
            self.table[r1] = r2
            self.table[r2] += d1


def main():
    n, k, l = map(int, sys.stdin.buffer.readline().split())
    a = UnionFind(n)
    b = UnionFind(n)
    cnt = 0
    for x in sys.stdin.buffer.readlines():
        p, q = map(int, x.split())
        cnt += 1
        if cnt <= k:
            a.union(p-1, q-1)
        else:
            b.union(p-1, q-1)

    pairs = [(a._root(i), b._root(i)) for i in range(n)]
    d = Counter(pairs)
    ans = [d[x] for x in pairs]
    print(*ans)


if __name__ == '__main__':
    main()
