mod = 10**9+7 #出力の制限
N = 2*10**5
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

import sys

sys.setrecursionlimit(10**4)

N=int(input())
edge=[[] for i in range(N)]
parent=[0]*N
deg=[1]*N
deg[0]=0
for i in range(N-1):
    x,y=map(int,input().split())
    edge[x-1].append(y-1)
    edge[y-1].append(x-1)


def prv(v,pv):
    for nv in edge[v]:
        if nv!=pv:
            parent[nv]=v
            prv(nv,v)

prv(0,-1)

for i in range(N):
    new=[]
    for v in edge[i]:
        if v!=parent[i]:
            new.append(v)
    edge[i]=new


from collections import deque
ans = list(v for v in range(N) if deg[v]==0)
deq = deque(ans)
used = [0]*N

while deq:
    v = deq.popleft()
    for t in edge[v]:
        deg[t] -= 1
        if deg[t]==0:
            deq.append(t)
            ans.append(t)


dp=[[] for i in range(N)]
sz=[0 for i in range(N)]

for v in ans[::-1]:
    sz[v]=1
    dp[v]=[0]*(sz[v]+1)
    dp[v][1]=1
    for nv in edge[v]:
        merged=[0]*(sz[v]+sz[nv]+1)
        for i in range(sz[v]+1):
            for j in range(sz[nv]+1):
                merged[i+j]=(merged[i+j]+dp[v][i]*dp[nv][j])%mod
        sz[v]+=sz[nv]
        dp[v] =merged
    for k in range(1,sz[v]+1):
        dp[v][0]=(dp[v][0]-(g1[k]*g2[k//2])%mod*((k+1)%2)*dp[v][k])%mod

print((-dp[0][0]*pow(inverse[2],N//2,mod))%mod)