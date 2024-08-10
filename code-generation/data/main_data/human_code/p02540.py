class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]


N = int(input())
L = []
for i in range(N):
    L.append(list(map(int,input().split())) + [i])
L.sort()

SUM1 = 0
SUM2 = 0
UFT = UnionFind(N)
for i in range(N-1):
    SUM1 += N - i
    SUM2 += L[i][1]
    if SUM1 != SUM2:
        UFT.union(i, i+1)
ans = [0] * N
for i in range(N):
    ans[L[i][2]] = UFT.size(i)
for i in range(N):
    print(ans[i])