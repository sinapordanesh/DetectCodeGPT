class DSUWeighted():
    def __init__(self, n):
        self.n = n
        self.par_size = [-1] * n
        self.wt = [0] * n

    def leader(self, a):
        #assert 0 <= a < self.n
        x = a
        order = [x]
        while self.par_size[x] >= 0:
            x = self.par_size[x]
            order.append(x)
        for s in order[:-1][::-1]:
            self.wt[s] += self.wt[self.par_size[s]]
            self.par_size[s] = x
        return x

    def same(self, a, b):
        #assert 0 <= a < self.n
        #assert 0 <= b < self.n
        return self.leader(a) == self.leader(b)

    def merge(self, a, b, w):
        #assert 0 <= a < self.n
        #assert 0 <= b < self.n
        x = self.leader(a)
        y = self.leader(b)
        w += self.wt[a] - self.wt[b]
        if x == y: return x
        if -self.par_size[x] < -self.par_size[y]:
            x, y = y, x
            w = -w
        self.par_size[x] += self.par_size[y]
        self.par_size[y] = x
        self.wt[y] = w
        return x

    def diff(self, x, y):
        return self.wt[y] - self.wt[x]

import sys
input = sys.stdin.buffer.readline

N, M = map(int, input().split())

uf = DSUWeighted(N)

for _ in range(M):
    l, r, d = map(int, input().split())
    if uf.same(l - 1, r - 1):
        if uf.diff(l - 1, r - 1) != d:
            print('No')
            break
    else:
        uf.merge(l - 1, r - 1, d)
else:
    print('Yes')