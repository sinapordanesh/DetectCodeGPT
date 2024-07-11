import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def dfs(u=0,pu=-1):
    if aa[u]<0:dp[u][0][0]=aa[u]
    else:dp[u][1][0]=aa[u]
    for v in to[u]:
        if v==pu:continue
        dfs(v,u)
        size[u]+=size[v]
        ndp0=[inf]*n
        ndp1=[inf]*n
        for k in range(size[u]):
            pre=dp[u][0][k]
            if pre==inf:continue
            for kv in range(size[v]):
                s=dp[v][0][kv]
                if s!=inf:ndp0[k+kv+1]=min(ndp0[k+kv+1],pre+s)
                if s<0:ndp0[k+kv]=min(ndp0[k+kv],pre)
                s = dp[v][1][kv]
                if s != inf: ndp0[k + kv+1] = min(ndp0[k + kv+1], pre + s)
                if s != inf: ndp0[k + kv] = min(ndp0[k + kv], pre)

        for k in range(size[u]):
            pre=dp[u][1][k]
            if pre==inf:continue
            for kv in range(size[v]):
                s=dp[v][0][kv]
                if s!=inf:ndp0[k+kv+1]=min(ndp0[k+kv+1],pre+s)
                if s<0:ndp1[k+kv]=min(ndp1[k+kv],pre)
                s = dp[v][1][kv]
                if s != inf: ndp1[k + kv+1] = min(ndp1[k + kv+1], pre + s)
                if s != inf: ndp1[k + kv] = min(ndp1[k + kv], pre)

        dp[u][0]=ndp0
        dp[u][1]=ndp1

inf=10**16
n=II()
aa=LI()
to=[[] for _ in range(n)]
for _ in range(n-1):
    u,v=MI1()
    to[u].append(v)
    to[v].append(u)

dp=[[[inf]*n for _ in range(2)] for _ in range(n)]
size=[1]*n
dfs()

mx=0
for k in range(n-1,-1,-1):
    if dp[0][0][k]<0:
        mx=max(mx,k)
        break
for k in range(n-1,-1,-1):
    if dp[0][1][k]!=inf:
        mx=max(mx,k)
        break
print(n-1-mx)
