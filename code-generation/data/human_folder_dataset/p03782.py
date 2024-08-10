n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
def f(x):
  if a[x]>=k:
    return True
  dp=[False]*k
  dp[0]=True
  y=0
  for i in range(n):
    if i==x:
      continue
    for j in range(y,-1,-1):
      if j+a[i]>=k:
        continue
      dp[j+a[i]]|=dp[j]
    y=min(k-1,y+a[i])
  return sum(dp[k-a[x]:k])
if not f(n-1):
  print(n)
  exit()
if f(0):
  print(0)
  exit()
l,r=0,n-1
while r-l>1:
  mid=(r+l)//2
  if f(mid):
    r=mid
  else:
    l=mid
print(r)
