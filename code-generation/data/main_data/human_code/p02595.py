def II(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

ans=0
N,D=MI()
D2=D*D
for i in range(N):
  x,y=MI()
  if x*x+y*y<=D2:
    ans+=1
print(ans)