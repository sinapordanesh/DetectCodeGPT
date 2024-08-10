N,M=map(int,input().split())
l=list(map(int,input().split()))
mem=[0]*N
def f(n):
   return n*(n-1)//2
s=0
for i in range(N):
   s+=l[i]
   mem[i]=s
mem=[i%M for i in mem]
from collections import Counter
mem=Counter(mem)
ans=mem[0]
mem=list(mem.values())
for i in mem:
   ans+=f(i)
print(ans)