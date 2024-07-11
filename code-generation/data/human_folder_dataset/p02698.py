import sys
sys.setrecursionlimit(10**7)
from bisect import bisect_left as bl
def main(n,a):
  ans=[0]*n
  ki=[[] for _ in range(n)]
  for _ in range(n-1):
    u,v=map(int,input().split())
    u,v=u-1,v-1
    ki[u].append(v)
    ki[v].append(u)
  inf=float('inf')
  p={}
  dp=[inf]*(n+1)
  dp[0]=0
  # dp[i]:長さiのLISの末尾の数値の最小値
  maxa=max(a)+1

  def dfs(v,p,dp):
    x=a[v]
    idx=bl(dp,x)
    tmp=dp[idx]
    dp[idx]=x
    # ans[v]=idx こっちだと頂点vで終わるLISの長さになる。下が正しい
    ans[v]=bl(dp,maxa)-1
    for nv in ki[v]:
      if nv==p:continue
      dfs(nv,v,dp)
    dp[idx]=tmp
  dfs(0,-1,dp)
  print(*ans,sep='\n')

n=int(input())
a=list(map(int,input().split()))
main(n,a)
