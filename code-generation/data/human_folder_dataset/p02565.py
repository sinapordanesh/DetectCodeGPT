N,D=map(int,input().split())
F=[tuple(map(int,input().split())) for i in range(N)]

EDGE=[[] for i in range(2*N)]
EDGE_INV=[[] for i in range(2*N)]

# 0～N : X_i
# N+1～2N: Y_i = ￢X_i

for i in range(N):
    x1,y1=F[i]

    for j in range(i,N):
        x2,y2=F[j]

        if abs(x1-x2)<D and i!=j:
            EDGE[i].append(N+j)
            EDGE[j].append(N+i)

            EDGE_INV[N+j].append(i)
            EDGE_INV[N+i].append(j)

        if abs(x1-y2)<D:
            EDGE[i].append(j)
            EDGE[N+j].append(N+i)

            EDGE_INV[j].append(i)
            EDGE_INV[N+i].append(N+j)

        if abs(y1-x2)<D:
            EDGE[N+i].append(N+j)
            EDGE[j].append(i)

            EDGE_INV[N+j].append(N+i)
            EDGE_INV[i].append(j)

        if abs(y1-y2)<D and i!=j:
            EDGE[N+i].append(j)
            EDGE[N+j].append(i)

            EDGE_INV[j].append(N+i)
            EDGE_INV[i].append(N+j)

QUE = list(range(2*N))
check=[0]*(2*N)
TOP_SORT=[]

def dfs(x):
    if check[x]==1:
        return
    check[x]=1
    
    for to in EDGE[x]:
        if check[to]==0:
            dfs(to)

    TOP_SORT.append(x) # 全ての点からDFSを行い, 帰りがけに点を答えに入れる
    check[x]=1

while QUE:
    x=QUE.pop()
    dfs(x)

USE=[0]*(2*N)
SCC=[]

def dfs2(x):
    Q=[x]
    USE[x]=1
    ANS=[]

    while Q:
        x=Q.pop()
        ANS.append(x)
        for to in EDGE_INV[x]:
            if USE[to]==0:
                USE[to]=1
                Q.append(to)
    return ANS

for x in TOP_SORT[::-1]:
    if USE[x]==0:
        SCC.append(dfs2(x))


PLACE=[-1]*(2*N)
for i in range(len(SCC)):
    for x in SCC[i]:
        PLACE[x]=i

ANS=[-1]*N
flag=1
for i in range(N):
    if PLACE[i]==PLACE[N+i]:
        flag=0
        break
    
    elif PLACE[i]>PLACE[N+i]:
        ANS[i]=F[i][0]
    else:
        ANS[i]=F[i][1]
    
if flag==0:
    print("No")
else:
    print("Yes")
    for ans in ANS:
        print(ans)
