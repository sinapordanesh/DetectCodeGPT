from collections import deque
import sys
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
E = []
for i in range(M):
    a, b, c = map(int, input().split())
    E.append((c, a-1, b-1))
E.sort()

*p, = range(N)
def root(x):
    if x == p[x]:
        return x
    p[x] = y = root(p[x])
    return y

L = 2*N-1
G = [[]] * L
C = [0]*L
*lb, = range(N)
cur = N

s = 0
for c, a, b in E:
    pa = root(a); pb = root(b)
    if pa == pb:
        continue
    s += c
    chds = [lb[pa], lb[pb]]
    if pa < pb:
        p[pb] = pa
        lb[pa] = cur
    else:
        p[pa] = pb
        lb[pb] = cur
    C[cur] = c
    G[cur] = chds
    cur += 1

H = [0]*L
prv = [-1]*L
def dfs(v):
    s = 1; heavy = -1; m = 0
    for w in G[v]:
        prv[w] = v
        c = dfs(w)
        if m < c:
            heavy = w
            m = c
        s += c
    H[v] = heavy
    return s
dfs(L-1)

SS = []
D = []
LB = [0]*L
I = [0]*L
que = deque([(L-1, 0)])
while que:
    v, d = que.popleft()
    S = []
    k = len(SS)
    while v != -1:
        I[v] = len(S)
        S.append(v)
        LB[v] = k
        h = H[v]
        for w in G[v]:
            if h == w:
                continue
            que.append((w, d+1))
        v = h
    SS.append(S)
    D.append(d)


def query(u, v):
    lu = LB[u]; lv = LB[v]
    dd = D[lv] - D[lu]
    if dd < 0:
        lu, lv = lv, lu
        v, u = u, v
        dd = -dd

    for _ in range(dd):
        v = prv[SS[lv][0]]
        lv = LB[v]

    while lu != lv:
        u = prv[SS[lu][0]]
        lu = LB[u]

        v = prv[SS[lv][0]]
        lv = LB[v]

    return u if I[u] < I[v] else v


def gen():
    Q = int(input())
    for i in range(Q):
        u, v = map(int, input().split())
        w = query(u-1, v-1)
        yield "%d\n" % (s - C[w])
ans = list(gen())
sys.stdout.writelines(ans)