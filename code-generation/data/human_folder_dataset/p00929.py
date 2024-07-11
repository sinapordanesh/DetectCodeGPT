N, M = map(int, input().split())
E0 = []
for i in range(M):
    S, D, C = map(int, input().split())
    E0.append((C, S-1, D-1))
E0.sort()

*parent, = range(N)
def root(x):
    if x == parent[x]:
        return x
    y = parent[x] = root(parent[x])
    return y
def unite(x, y):
    px = root(x); py = root(y)
    if px < py:
        parent[py] = px
    else:
        parent[px] = py
cnt = 0; base = None
for i in range(M):
    C, S, D = E0[i]
    if root(S) != root(D):
        unite(S, D)
        cnt += 1
        if cnt == N-1:
            base = C
ES = {}; CM = {}
for i in range(M):
    C, S, D = E0[i]
    if C <= base:
        ES.setdefault(C, set()).add((S, D))
        CM[S, D] = C
def bridge(G, N):
    result = set()
    label = [None]*N
    gen = 0
    cost = [0]*N
    def dfs(u, p):
        nonlocal gen
        res = 0
        for v in G[u]:
            if v == p:
                continue
            if label[v] is not None:
                if label[v] < label[u]:
                    cost[v] += 1
                    res += 1
            else:
                label[v] = gen; gen += 1
                r = dfs(v, u)
                if r == 0:
                    result.add((u, v) if u < v else (v, u))
                res += r
        res -= cost[u]
        return res
    for v in range(N):
        if not label[v]:
            label[v] = gen; gen += 1
            r = dfs(v, -1)
            assert r == 0, r
    return result
G = [[] for i in range(N)]
cnt = 0; ans = 0
for C in sorted(ES):
    for S, D in ES[C]:
        G[S].append(D)
        G[D].append(S)
    B = bridge(G, N)
    cnt += len(B & ES[C])
    ans += len(B & ES[C]) * C
print(cnt, ans)