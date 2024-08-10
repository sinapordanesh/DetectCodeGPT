import sys
sys.setrecursionlimit(10**7)
inf=float('inf')

def main(n,m,g,uv):
    # 1<=E<=n-1
    eary=[inf]*m
    vary=[inf]*n
    vary[-1]=0
    todo=[n-1]
    def dfs(v,x):
        if vary[v]<inf:return vary[v]
        ret=0
        cnt=0
        for i,nv in g[v]:
            if i==x:continue
            tmp=dfs(nv,x)+1
            eary[i]=tmp
            ret+=tmp
            cnt+=1
        if cnt==0:
            for i in range(n):
                vary[i]=inf
            return inf
        vary[v]=ret/cnt
        return ret/cnt
    e0=dfs(0,-1)
    ary=[-1]*m
    bary=[0]*n
    bary[0]=1
    for v in range(n):
        k=len(g[v])
        e=vary[v]
        for i,nv in g[v]:
            bary[nv]+=1/k*bary[v]
            if k>1 and bary[v]:
                ary[i]=max(0,e-(e*k-eary[i])/(k-1))
                ary[i]*=bary[v]
    return e0-max(0,max(ary))

n,m=map(int,input().split())
uv=[list(map(int,input().split())) for _ in range(m)]
g=[[] for _ in range(n)]
for i,(u,v) in enumerate(uv):
    u,v=u-1,v-1
    g[u].append((i,v))
print(main(n,m,g,uv))
