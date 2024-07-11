import sys
from operator import itemgetter

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

class UnionFind:
    def __init__(self, N):
        self.root = list(range(N + 1))

    def __getitem__(self, x):
        root = self.root
        while root[x] != x:
            root[x] = root[root[x]]
            x = root[x]
        return x

    def merge(self, x, y):
        x = self[x]
        y = self[y]
        if x == y:
            return
        # 番号の大きい頂点を根にする
        if x < y:
            x, y = y, x
        self.root[y] = x

N = int(readline())
m = map(int, read().split())
ABC = sorted(zip(m, m, m), key=itemgetter(2), reverse=True)

uf = UnionFind(N + N)
parent = [0] * (N + N)
value = [0] * (N + N)
for n, (a, b, c) in enumerate(ABC, N + 1):
    ra = uf[a]
    rb = uf[b]
    parent[ra] = n
    parent[rb] = n
    value[n] = c
    uf.merge(ra, n)
    uf.merge(rb, n)

size = [0] + [1] * N + [0] * (N - 1)
for n in range(N + N):
    p = parent[n]
    size[p] += size[n]

for n in range(N + N):
    p = parent[n]
    value[n] = 0
    if not p:
        continue
    value[n] = value[p] * (size[p] - size[n])
for n in range(N + N - 2, 0, -1):
    p = parent[n]
    value[n] += value[p]

print('\n'.join(map(str, value[1:N + 1])))