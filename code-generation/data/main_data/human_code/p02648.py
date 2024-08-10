import sys,random,time,bisect
input=sys.stdin.buffer.readline

start=time.time()
N=int(input())
vw=[(-1,-1)]
for i in range(N):
    vw.append(tuple(map(int,input().split())))

dp=[[] for i in range(2**9)]
def make_dp(v):
    t=[[0,0] for i in range(15)]
    V=v
    id=0
    while v>=1:
        t[id]=vw[v]
        id+=1
        v//=2
    n=id
    temp=[[0,0] for i in range(2**n)]
    for i in range(n):
        for j in range(2**i,2**(i+1)):
            temp[j][0]=temp[j-2**i][0]+t[i][0]
            temp[j][1]=temp[j-2**i][1]+t[i][1]
    temp.sort(key=lambda x:x[1])
    while temp and temp[-1][1]>10**5:
        temp.pop()
    m=len(temp)
    for i in range(1,m):
        temp[i][0]=max(temp[i][0],temp[i-1][0])

    dp[V]=[0]*(10**5+1)
    for i in range(m-1):
        L=temp[i][1]
        R=temp[i+1][1]
        for j in range(L,R):
            dp[V][j]=temp[i][0]
    else:
        L=temp[-1][1]
        for j in range(L,10**5+1):
            dp[V][j]=temp[-1][0]

MAX=min(2**9,N+1)
for i in range(1,MAX):
    make_dp(i)

Q=int(input())
query=[[] for i in range(N+1)]
for i in range(Q):
    v,L=map(int,input().split())
    query[v].append((L,i))

ans=[0]*Q
temp=[[0,0] for i in range(2**9)]
t=[[0,0] for i in range(15)]
def solve(v):
    V=v
    id=0
    while v>=2**9:
        t[id]=vw[v]
        id+=1
        v//=2
    n=id
    for i in range(n):
        for j in range(2**i,2**(i+1)):
            temp[j][0]=temp[j-2**i][0]+t[i][0]
            temp[j][1]=temp[j-2**i][1]+t[i][1]

    for L,ID in query[V]:
        res=0
        for i in range(2**n):
            if L>=temp[i][1]:
                res=max(res,temp[i][0]+dp[v][L-temp[i][1]])
        ans[ID]=res

for i in range(1,N+1):
    if query[i]:
        solve(i)

for i in range(Q):
    print(ans[i])
