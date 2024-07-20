from collections import deque
N, M = map(int, input().split())
route = [[] for _ in range(N)]
for _ in range(M):
  A, B = map(int, input().split())
  route[A-1].append(B-1)
  route[B-1].append(A-1)
ans = [-1]*(N)

def bfs():
  tmp = 0
  prv = 0
  visited = [False]*N
  kouho = deque()


  for room in route[0]:
    kouho.append([room,0])
  while True:
    visited[tmp] = True
    ans[tmp] = prv
    for room in route[tmp]:
      if not visited[room]:
        kouho.append([room,tmp])
    if len(kouho) == 0:
      return
    while True:
      tmp_ = kouho.popleft()
      tmp = tmp_[0]
      prv = tmp_[1]
      if not visited[tmp]:
        break
      if len(kouho) == 0:
        return
bfs()
print("Yes")
for n in range(1,N):
  print(ans[n]+1)
  

