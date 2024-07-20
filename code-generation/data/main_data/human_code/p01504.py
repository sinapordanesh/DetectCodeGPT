import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve(t):
    N, T, K = map(int, readline().split())
    if N == T == K == 0:
        return False
    G = [[] for i in range(N)]
    E = []
    res = 0
    for i in range(N-1):
        a, b, c = map(int, readline().split())
        res += c
        E.append((c, a-1, b-1))
    E.sort(reverse=1)
    sz = [0]*N
    for i in range(T):
        v = int(readline())-1
        sz[v] = 1
    *prt, = range(N)
    def root(x):
        if x == prt[x]:
            return x
        prt[x] = y = root(prt[x])
        return y
    def unite(x, y):
        px = root(x); py = root(y)
        if px < py:
            prt[py] = px
            sz[px] += sz[py]
        else:
            prt[px] = py
            sz[py] += sz[px]
    d = T - K - 1
    for c, a, b in E:
        pa = root(a); pb = root(b)
        if sz[pa] == 0 or sz[pb] == 0:
            unite(a, b)
            res -= c
            continue
        if d > 0:
            d -= 1
            unite(a, b)
            res -= c
    write("Case %d: %d\n" % (t, res))
    return True
i = 1
while solve(i):
    i += 1
