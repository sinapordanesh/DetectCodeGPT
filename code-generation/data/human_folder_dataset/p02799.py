import sys

input=sys.stdin.buffer.readline
sys.setrecursionlimit(2*10**5)

N,M=map(int,input().split())
D=list(map(int,input().split()))
edge=[[] for i in range(N)]
for i in range(M):
    u,v=map(int,input().split())
    edge[u-1].append((v-1,i))
    edge[v-1].append((u-1,i))

used=[False]*N
color=[-1 for i in range(N)]
C=[10**9 for i in range(M)]
for v in range(N):
    if not used[v]:
        for nv,id in edge[v]:
            if D[nv]<D[v]:
                break
        else:
            for nv,id in edge[v]:
                if D[nv]==D[v]:
                    C[id]=D[v]
                    used[v]=True
                    if not used[nv]:
                        color[nv]=0
                        color[v]=1
                        used[nv]=True
                    else:
                        color[v]=1-color[nv]
                    break
            else:
                exit(print(-1))
Edge=[]
for v in range(N):
    if not used[v]:
        used[v]=True
        for nv,id in edge[v]:
            if D[nv]<D[v]:
                C[id]=D[v]-D[nv]
                Edge.append((v,nv,id))
                break

parent=[-1]*N
for u,v,id in Edge:
    parent[u]=v

def Coloring(v):
    if color[v]!=-1:
        return color[v]
    else:
        color[v]=Coloring(parent[v])
        return color[v]

res=[""]*N
for i in range(N):
    if Coloring(i)==0:
        res[i]="W"
    else:
        res[i]="B"

print("".join(res))
for i in range(M):
    print(C[i])
