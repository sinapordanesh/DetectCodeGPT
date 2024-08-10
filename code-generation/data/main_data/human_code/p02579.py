from collections import deque
import sys

H, W = map(int, input().split())
xs, ys = map(int, input().split())
xt, yt = map(int, input().split())
xs -= 1
ys -= 1
xt -= 1
yt -= 1
G = [input() for _ in range(H)]

D_wk = [[1,0], [0,1], [-1,0], [0,-1]]
D_tl = 2

#cost = [[-1  for _ in range(W)] for _ in range(H)]

possible = set()
for i in range(H):
  for j in range(W):
    if G[i][j] == ".":
      possible.add(i * W + j)

# 01-BFS
def append_walk(c, x, y):
  for dx, dy in D_wk:
    if 0 <= x+dx <= H-1 and 0 <= y+dy <= W-1 and ((x+dx)*W+(y+dy)) in possible and ((x+dx)*W+(y+dy)) not in visited:
      task.appendleft([c, x+dx, y+dy])
def append_tele(c, x, y):
  for dx in range(-D_tl, D_tl+1):
    for dy in range(-D_tl, D_tl+1):
      if 0 <= x+dx <= H-1 and 0 <= y+dy <= W-1 and ((x+dx)*W+(y+dy)) in possible and ((x+dx)*W+(y+dy)) not in visited:
        task.append([c+1, x+dx, y+dy])

task = deque([[0, xs, ys]])
visited = set()
while task:
  while True:
    c, x, y = task.popleft()
    if x*W+y not in visited:
      break
    if not task:
      print(-1)
      sys.exit()    
  if x == xt and y == yt:
    print(c)
    #print(*cost, sep="\n")
    sys.exit()  
  visited.add(x*W+y)
  #cost[x][y] = c
  append_walk(c, x, y)
  append_tele(c, x, y)
  
print(-1)