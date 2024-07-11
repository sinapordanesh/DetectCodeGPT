import sys
from bisect import bisect, bisect_left


class BinaryIndexedTree:
    def __init__(self, n):
        self.size = n
        self.INF = 10 ** 18
        self.tree = [self.INF] * (n + 1)

    def get_min(self, i):
        s = self.INF
        while i > 0:
            s = min(s, self.tree[i])
            i -= i & -i
        return s

    def update(self, i, x):
        while i <= self.size:
            if self.tree[i] <= x:
                break
            self.tree[i] = x
            i += i & -i


def solve(n, e, t, xxx):
    if n == 1:
        return e + t

    dp1 = [0] * (n + 1)
    dp2 = BinaryIndexedTree(n + 1)
    dp2.update(1, -xxx[0] * 2)

    for i in range(n):
        x = xxx[i]
        j = bisect_left(xxx, x - t // 2, hi=i)
        ex_time = dp1[j] + t
        if j > 0:
            ex_time = min(ex_time, x * 2 + dp2.get_min(j))
        dp1[i + 1] = ex_time
        if i < n - 1:
            dp2.update(i + 2, ex_time - xxx[i + 1] * 2)

    return e + dp1[-1]


n, e, t, *xxx = map(int, sys.stdin.buffer.read().split())
print(solve(n, e, t, xxx))
