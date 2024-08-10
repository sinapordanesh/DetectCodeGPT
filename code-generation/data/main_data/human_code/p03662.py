import sys
sys.setrecursionlimit(10**7)
n=int(input())
edge=[[] for _ in range(n)]
for i in range(n-1):
    x,y=map(int,input().split())
    edge[x-1].append(y-1)
    edge[y-1].append(x-1)
def dfs(node,dist,distl):
    distl[node]=dist
    for e in edge[node]:
        if distl[e]==-1:
            dfs(e,dist+1,distl)
dista,distb=[-1]*n,[-1]*n
dfs(0,0,dista)
dfs(n-1,0,distb)
a,b=0,0
for i in range(n):
    if dista[i]<=distb[i]:
        a+=1
    else:
        b+=1
print('Fennec' if a>b else 'Snuke')