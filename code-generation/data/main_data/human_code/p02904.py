n,k=map(int,input().split())
p=list(map(int,input().split()))
from heapq import heappop,heappush,heapify


import heapq
class pqheap:
  def __init__(self,key=None):
    self.p = list()
    self.q = list()

  def insert(self,x):
    heapq.heappush(self.p, x)
    return

  def erase(self,x):
    heapq.heappush(self.q, x)
    return

  def minimum(self):
    while self.q and self.p[0] == self.q[0]:
      heapq.heappop(self.p)
      heapq.heappop(self.q)
    return self.p[0] if len(self.p)>0 else None
minheap=pqheap()
maxheap=pqheap()
for i in range(k):
  minheap.insert(p[i])
  maxheap.insert(-p[i])
ans=1
premin=minheap.minimum()
premax=-maxheap.minimum()

for i in range(k,n):
  ins=p[i]
  era=p[i-k]
  minheap.erase(era)
  maxheap.erase(-era)
  minheap.insert(ins)
  maxheap.insert(-ins)
  if premin==era and ins==-maxheap.minimum():
    pass
  else:
    ans+=1
  premax=-maxheap.minimum()
  premin=minheap.minimum()
ans0=0
now=1
pre=p[0]
for x in p[1:]:
  if x>pre:
    now+=1
  else:
    now=1
  if now==k:
    ans0+=1
  pre=x


print(ans-max(0,ans0-1))
