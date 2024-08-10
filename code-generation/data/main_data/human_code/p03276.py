import sys
def input():
  return sys.stdin.readline().rstrip()

N,K=map(int,input().split())
x=list(map(int,input().split()))

ans=1<<60
for i in range(N-K+1):
  left=x[i]
  right=x[i+K-1]
  a=min(abs(left),abs(right))+right-left
  ans=min(ans,a)

print(ans)
