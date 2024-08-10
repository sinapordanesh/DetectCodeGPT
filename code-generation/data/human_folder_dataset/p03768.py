N, M = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(M)]
Q = int(input())
vdc = [list(map(int, input().split())) for _ in range(Q)]

L = [[] for _ in range(N)]
for a, b in ab:
  a -= 1
  b -= 1
  L[a].append(b)
  L[b].append(a)

D = [[0] * 11 for _ in range(N)]
Ans = [0] * N

def check(v, d, c):
  if D[v][d] != 0: return
  if d == 0:
    D[v][d] = c
    return
  for i in range(d, -1, -1):
    if D[v][i] != 0: break
    D[v][i] = c
  for i in L[v]:
    pass

import queue
Que = queue.Queue
get = queue.Queue.get
put = queue.Queue.put
emp = queue.Queue.empty

for v, d, c in vdc[::-1]:
  v -= 1
  if D[v][d] != 0: continue
  t = (d << 18) + v
  S = Que()
  put(S, t)
  while not emp(S):
    t = get(S)
    dd = t >> 18
    vv = t & ((1 << 18) - 1)
    if Ans[vv] == 0: Ans[vv] = c
    if dd == 0:
      D[vv][dd] = c
      continue
    for i in range(dd, -1, -1):
      if D[vv][i] != 0: break
      D[vv][i] = c
    for i in L[vv]:
      if D[i][dd - 1] != 0: continue
      t = ((dd - 1) << 18) + i
      put(S, t)

for i in Ans:
  print(i)