class dsu:
    def __init__(self, n=0):
        self._n = n
        self.parent_or_size = [-1] * n
    
    def merge(self, a: int, b: int) -> int:
        x = self.leader(a)
        y = self.leader(b)
        if x == y:
            return x
        if self.parent_or_size[x] > self.parent_or_size[y]:
            x, y = y, x
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        return x
    
    def same(self, a: int, b: int) -> bool:
        return self.leader(a) == self.leader(b)
    
    def leader(self, a: int) -> int:
        x = a
        while self.parent_or_size[x] >= 0:
            x = self.parent_or_size[x]
        while a != x:
            self.parent_or_size[a], a = x, self.parent_or_size[a]
        return x
    
    def size(self, a: int) -> int:
        return -self.parent_or_size[self.leader(a)]
    
    def groups(self):
        g = [[] for _ in range(self._n)]
        for i in range(self._n):
            g[self.leader(i)].append(i)
        return list(c for c in g if c)

n, m = map(int, input().split())
vdata = [] # (required, gain)
for _ in range(n):
    a, b = map(int, input().split())
    vdata.append((max(a - b, 0), b))
to = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    to[u].append(v)
    to[v].append(u)
s = dsu(n)
dp = vdata.copy() # (extra, tot_gain)
visited = [False] * n
for u in sorted(range(n), key=lambda i: vdata[i][0]):
    req, gain = vdata[u]
    frm = {u}
    for v in to[u]:
        if visited[v]:
            frm.add(s.leader(v))
    mnextra = 10 ** 18
    for v in frm:
        e, g = dp[v]
        e += max(req - (e + g), 0)
        if e < mnextra:
            mnextra, mni = e, v
    extra, tot_gain = mnextra, sum(dp[v][1] for v in frm)
    for v in frm:
        s.merge(u, v)
    dp[s.leader(u)] = extra, tot_gain
    visited[u] = True
ans = sum(dp[s.leader(0)])
print(ans)
