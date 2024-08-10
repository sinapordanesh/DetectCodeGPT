N = int(input())
X = list(map(int, input().split()))
L = int(input())
from bisect import *
def get_move(X,L,left=False):
  res = [0]*N
  for i in range(N):
    if left:
      res[i] = bisect_left(X,X[i]-L)
    else:
      res[i] = bisect_right(X,X[i]+L)-1
  K = N.bit_length()
  db = [[0]*N for _ in range(K)]
  db[0] = res
  for i in range(1,K):
    for j in range(N):
      db[i][j] = db[i-1][db[i-1][j]]
  return db

def search(dbr,dbl,a,b):
  if a>b:
    db = dbl
    left = True
  else:
    db = dbr
    left = False
  K = N.bit_length()
  ans = 0
  for p in range(K-1,-1,-1):
    if left:
      if b < db[p][a]:
        a = db[p][a]
        ans += 1<<p
    else:
      if b > db[p][a]:
        a = db[p][a]
        ans += 1<<p
  ans += 1
  return ans

dbr = get_move(X,L)
dbl = get_move(X,L,left=True)
Q = int(input())
ans = [0]*Q
for i in range(Q):
  a,b = map(int, input().split())
  ans[i] = search(dbr,dbl,a-1,b-1)
print(*ans, sep='\n')
