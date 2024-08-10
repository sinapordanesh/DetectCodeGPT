import sys
def input():
  return sys.stdin.readline().rstrip()

N=int(input())
L=sorted(list(map(int,input().split())))

ans=0
for i in range(0,2*N,2):
  ans+=L[i]

print(ans)
