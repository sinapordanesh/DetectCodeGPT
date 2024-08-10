n,m=map(int,input().split())
g=[[] for _ in range(n)]
for _ in range(m):
    u,v=map(int,input().split())
    u,v=u-1,v-1
    g[u].append(v)

import sys
sys.setrecursionlimit(10**7)

def func(loop):
    sl=set(loop)
    k=len(loop)
    for i in range(k):
        v=loop[i]
        for nv in g[v]:
            if nv not in sl:continue
            if nv==loop[(i+1)%k]:continue
            j=[j for j in range(k) if loop[j]==nv][0]
            if i<j:
                ary=loop[:i+1]+loop[j:]
            else:
                ary=loop[j:i+1]
            func(ary)
    print(len(loop))
    for x in loop:
        print(x+1)
    exit()

mi=set(range(n))
def dfs(v,par):
    mi.discard(v)
    for nv in g[v]:
        if par[nv]==-1:
            par[nv]=v
            dfs(nv,par)
            par[nv]=-1
        else:
            loop=[v]
            while v!=nv:
                loop.append(par[v])
                v=par[v]
            loop.reverse()
            func(loop)
while mi:
    v=mi.pop()
    dfs(v,[-1]*n)
print(-1)
