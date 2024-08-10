import sys
sys.setrecursionlimit(10**5)
def dfs(now):
  if v[now]:return v[now]
  res=1
  for to in e[now]:
    res=max(res,dfs(to)+1)
  v[now]=res
  return res
n,m=map(int,input().split())
e=[[]for _ in range(n+1)]
for i in range(m):
  x,y=map(int,input().split())
  e[x]+=[y]
v=[0]*(n+1)
v[0]=1
ans=0
for i in range(n+1):
  ans=max(ans,dfs(i))
print(ans-1)