from bisect import bisect_left
from collections import defaultdict
N=int(input())
D=[[] for i in range(2*10**5+1)]
U=[[] for i in range(2*10**5+1)]
L=[[] for i in range(2*10**5+1)]
R=[[] for i in range(2*10**5+1)]
arr=[]


T=[[[] for i in range(2*10**5+1)] for i in range(4)]
li=['U','L','D','R']
for i in range(N):
    X,Y,v=input().split()
    X,Y=int(X),int(Y)
    arr.append((X,Y,v))
    if v=='U':
        U[X].append(Y)
    if v=='D':
        D[X].append(Y)
    if v=='L':
        L[Y].append(X)
    if v=='R':
        R[Y].append(X)
ans=float('inf')
for i in range(2*10**5+1):
    D[i].sort()
    for u in U[i]:
        b=bisect_left(D[i],u)
        if b==len(D[i]):
            continue
        ans=min(ans,5*(D[i][b]-u))
    L[i].sort()
    for r in R[i]:
        b=bisect_left(L[i],r)
        if b==len(L[i]):
            continue
        ans=min(ans,5*(L[i][b]-r))
        
def check(R,U):
    res=float('inf')
    for A,B in U.items():
        B.sort()
    for xr,yr in R:
        b=bisect_left(U[xr+yr],xr)
        if b==len(U[xr+yr]):
            continue
        res=min(res,10*(U[xr+yr][b]-xr))
    return res

def f1(x,y):return x,y
def f2(x,y):return -y,x
def f3(x,y):return -x,-y
def f4(x,y):return y,-x
fanc=[f1,f2,f3,f4]
for t in range(4):
    arr2=[]
    for x,y,v in arr:
        a,b=fanc[t](x,y)
        c=li[(li.index(v)+t)%4]
        arr2.append((a,b,c))
    r2,u2=[],defaultdict(list)
    for x,y,v in arr2:
        if v=='R':
            r2.append((x,y))
        if v=='U':
            u2[x+y].append(x)
    ans=min(ans,check(r2,u2))
print(ans if ans!=float('inf') else 'SAFE')