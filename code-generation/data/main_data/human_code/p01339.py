import sys
readline = sys.stdin.readline
write = sys.stdout.write
sys.setrecursionlimit(10**6)
def scc(N, G, RG):
    order = []
    used = [0]*N
    group = [None]*N
    def dfs(s):
        used[s] = 1
        for t in G[s]:
            if not used[t]:
                dfs(t)
        order.append(s)
    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        for t in RG[s]:
            if not used[t]:
                rdfs(t, col)
    for i in range(N):
        if not used[i]:
            dfs(i)
    used = [0]*N
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, group

def construct(N, G, label, group):
    G0 = [set() for i in range(label)]
    GP = [[] for i in range(label)]
    for v in range(N):
        lbs = group[v]
        for w in G[v]:
            lbt = group[w]
            if lbs == lbt:
                continue
            G0[lbs].add(lbt)
        GP[lbs].append(v)
    return G0, GP

N, M = map(int, readline().split())
G = [[] for i in range(N)]
RG = [[] for i in range(N)]
for i in range(M):
    s, d = map(int, readline().split()); s -= 1; d -= 1
    G[d].append(s)
    RG[s].append(d)

N0, group = scc(N, G, RG)
G0, GP = construct(N, G, N0, group)

deg = [0]*N0
for v in range(N0):
    for w in G0[v]:
        deg[w] += 1
MOD = 10**9 + 7
def dfs(v):
    r = 1
    for w in G0[v]:
        r = r * dfs(w) % MOD
    return r + 1
ans = 1
for v in range(N0):
    if deg[v] == 0:
        ans = ans * dfs(v) % MOD
write("%d\n" % ans)
