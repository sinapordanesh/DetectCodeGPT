import sys

N=int(input())
edge=[[] for i in range(N)]
for i in range(N-1):
    a,b=map(int,input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

ans=(10**15,10**15)

root=-1
depth=[0]*N
Mdata=[0]*100

def dfs(v,pv):
    for nv in edge[v]:
        if nv!=pv:
            depth[nv]=depth[v]+1
            Mdata[depth[nv]]=max(Mdata[depth[nv]],len(edge[nv])-1)
            dfs(nv,v)

for i in range(N):
    depth=[0]*N
    Mdata=[0]*100
    Mdata[0]=len(edge[i])
    dfs(i,-1)
    tempc=max(depth)+1
    res=1
    for j in range(N):
        if Mdata[j]!=0:
            res*=Mdata[j]
        else:
            break
    ans=min(ans,(tempc,res))

#print(ans)

for i in range(N):
    for j in edge[i]:
        depth=[0]*N
        Mdata=[0]*100
        depth[i]=1
        depth[j]=1
        Mdata[1]=max(len(edge[i]),len(edge[j]))-1
        Mdata[0]=2
        dfs(i,j)
        dfs(j,i)
        tempc=max(depth)
        res=1
        for k in range(N):
            if Mdata[k]!=0:
                res*=Mdata[k]
            else:
                break
        ans=min(ans,(tempc,res))

print(*ans)