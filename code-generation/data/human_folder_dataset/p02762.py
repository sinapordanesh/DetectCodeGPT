from sys import setrecursionlimit
setrecursionlimit(1 << 30)

nv, ne, nBad = map(int, input().split())
g = [[] for _ in range(nv)]
for _ in range(ne):
    u, v = map(lambda x: int(x) - 1, input().split())
    g[u].append(v)
    g[v].append(u)
a = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(nBad)]

def dfs(v):
    id[v] = cur
    comps[-1].append(v)
    for to in g[v]:
        if id[to] == None:
            dfs(to)

id = [None] * nv
cur = 0
comps = []
for v in range(nv):
    if id[v] == None:
        comps.append([])
        dfs(v)
        cur += 1
bad = [0] * nv
for u, v in a:
    if id[u] == id[v]:
        bad[u] += 1
        bad[v] += 1
ret = [None] * nv
for v in range(nv):
    ret[v] = len(comps[id[v]]) - 1 - len(g[v]) - bad[v]
print(' '.join(map(str, ret)))