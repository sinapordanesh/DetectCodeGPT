def A():
    d, t, s = map(int, input().split())
    print("Yes" if t*s>=d else "No")

def B():
    s = input()
    t = input()
    sa = len(s) - len(t)
    ret = 10000000000
    for i in range(sa+1):
        cnt = 0
        for j in range(len(t)):
            if s[j+i] != t[j]: cnt += 1
        ret = min(ret, cnt)
    print(ret)

def C():
    int(input())
    A = list(map(int, input().split()))
    S = sum(A)
    T = 0
    for e in A:
        T += e*e
    print((S * S - T)//2)

class UF:
    def __init__(self, N):
        self.N = N
        self.sz = [1] * N
        self.par = [i for i in range(N)]
        self.d = [1] * N

    def find(self, x):
        if self.par[x] == x: return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return False
        if self.d[y] > self.d[x]:
            self.par[x] = y
            self.sz[y] += self.sz[x]
        else:
            self.par[y] = x
            self.sz[x] += self.sz[y]
            if self.d[x] == self.d[y]: self.d[x] += 1

def D():
    n, m = map(int, input().split())
    uf = UF(n+1)
    for i in range(m):
        a, b = map(int, input().split())
        uf.unite(a, b)
    print(max(uf.sz))

D()
