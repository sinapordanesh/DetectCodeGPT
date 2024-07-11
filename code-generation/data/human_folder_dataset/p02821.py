N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
from bisect import bisect_left
def isok(n):
  sum=0
  for i in range(N):
    sum+=N-bisect_left(A,n-A[i])
  return sum>=M
start,end=0,2*10**5+1
while end-start>1:
  mid=(start+end)//2
  if isok(mid):
    start=mid
  else:
    end=mid
b=[A[0]]
for i in range(1,N):
  b.append(b[-1]+A[i])
l=0
ans=0
bn=b[N-1]
for i in range(N):
  a=bisect_left(A,start-A[i])
  l+=N-a
  if a>0:
    ans+=A[i]*(N-a)+bn-b[a-1]
  else:
    ans+=A[i]*(N-a)+bn
ans-=start*(l-M)
print(ans) 