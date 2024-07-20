G=[]
def g(x):
  global G
  G=[]
  for i in range(51):
    G.append([])
    for j in range(1,i+1):
      if x&(1<<j):
        G[i].append((i%j,0))

from heapq import *
D=[0]*51
INF=1000
def ijk(s):
  for i in range(len(G)):
    D[i]=INF
  D[s]=0
  Q=[]
  heapify(Q)
  heappush(Q,(0,s))
  p,v,e=0,0,0
  while len(Q):
    p=heappop(Q)
    v=p[1]
    if D[v]<p[0]:
      continue
    for i in range(len(G[v])):
      e=G[v][i]
      if D[e[0]]>D[v]+e[1]:
        D[e[0]]=D[v]+e[1]
        heappush(Q,(D[e[0]],e[0]))

N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
def j(x):
  g(x)
  for i in range(N):
    ijk(A[i])
    if D[B[i]]>=INF:
      return 0
  return 1

X=-1
for i in range(1,52):
  if j((1<<i)-1):
    X=(1<<i)-1
    break
if X==-1:
  print(-1)
  exit()
for i in range(51,-1,-1):
  if X&(1<<i):
    if j(X^(1<<i)):
      X^=(1<<i)
print(X)