class Unionfindtree:
    def __init__(self, number):
        self.par = [i for i in range(number)]
        self.rank = [0] * (number)

    def find(self, x):  # 親を探す
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):  # x,yを繋げる
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.par[px] = py
        else:
            self.par[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

    def connect(self, x, y):  # 親が同じかみる
        return self.find(x) == self.find(y)


N, M, K = map(int, input().split())
C = [int(i) for i in input().split()]
table = []
t = K
for i in range(N):
    if C[i]==0:
        t+=1
        C[i]=t
for i in range(M):
    s, u, c = map(int, input().split())
    a, b = C[s - 1], C[u - 1]
    table.append((c, a, b))

tree = Unionfindtree(t+1)
table.sort()
ct = K - 1
ans = 0
for c, a, b in table:
    if not tree.connect(a, b) and ct > 0:
        tree.union(a, b)
        ans += c
        ct -= 1
if ct > 0:
    print(-1)
else:
    print(ans)

