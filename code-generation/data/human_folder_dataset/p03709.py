class BIT():
    def __init__(self,n,mod):
        self.BIT=[0]*(n+1)
        self.num=n
        self.mod=mod

    def query(self,idx):
        res_sum = 0
        mod=self.mod
        while idx > 0:
            res_sum += self.BIT[idx]
            res_sum%=mod
            idx -= idx&(-idx)
        return res_sum

    #Ai += x O(logN)
    def update(self,idx,x):
        mod=self.mod
        while idx <= self.num:
            self.BIT[idx] += x
            self.BIT[idx]%=mod
            idx += idx&(-idx)
        return

import sys,bisect

input=sys.stdin.readline

mod=10**9+7
inv=pow(2,mod-2,mod)

N=int(input())
taka=[tuple(map(int,input().split())) for i in range(N)]
taka.sort()

V=[0]+[taka[i][1] for i in range(N)]+[10**15]
cummin=[V[i] for i in range(N+2)]
for i in range(N,-1,-1):
    cummin[i]=min(cummin[i],cummin[i+1])
cummax=[V[i] for i in range(N+2)]
for i in range(1,N+2):
    cummax[i]=max(cummax[i],cummax[i-1])

const=[]
for i in range(1,N+1):
    R=bisect.bisect_right(cummin,V[i])-1
    L=bisect.bisect_left(cummax,V[i])
    const.append((L,R))


Lconst=[(i,10**15) for i in range(N+1)]
for L,R in const:
    pL,pR=Lconst[L]
    Lconst[L]=(L,min(R,pR))

_const=[]
for i in range(1,N+1):
    L,R=Lconst[i]
    if R!=10**15:
        _const.append((L,R))

const=[]
for L,R in _const:
    while const and const[-1][1]>=R:
        const.pop()
    const.append((L,R))


M=len(const)
const=[(-10**15,0)]+const
Rconst=[const[i][1] for i in range(M+1)]
B=BIT(M,mod)
dp=[1]*(M+1)
for i in range(1,M+1):
    L,R=const[i]
    id=bisect.bisect_left(Rconst,L)
    res=(B.query(i-1)-B.query(id-1))%mod
    l,r=const[id]
    l=max(l,Rconst[id-1]+1)
    res+=dp[id-1]*(pow(2,r-L+1,mod)-1)*pow(2,L-l,mod)%mod
    res%=mod
    dp[i]=res
    if i!=M:
        nR=Rconst[i+1]
        add=dp[i]*(pow(2,nR-R,mod)-1)%mod
        add%=mod
        B.update(i,add)

cnt=0
data=[0]*(N+2)
for i in range(1,M+1):
    L,R=const[i]
    data[L]+=1
    data[R+1]+=-1
for i in range(1,N+2):
    data[i]+=data[i-1]
for i in range(1,N+1):
    if data[i]==0:
        cnt+=1
ans=pow(2,cnt,mod)*dp[M]
ans%=mod
print(ans)
