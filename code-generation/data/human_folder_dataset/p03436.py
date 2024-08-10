from collections import deque

def bfs(sy,sx):
  q = deque([[sy,sx]])
  d[sy][sx] = 0
  while q:
    y,x = q.popleft()
    for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
      dy,dx = y+i,x+j
      if dy < 0 or h <= dy: continue
      elif dx < 0 or w <= dx: continue
      elif s[dy][dx] == "#": continue
      elif d[dy][dx] != -1: continue
      d[dy][dx] = d[y][x]+1
      q.append([dy,dx])

h,w = map(int, input().split())
s = [input() for _ in range(h)]

if s[0][0] == "#" or s[h-1][w-1] == "#":
  print(-1)
  exit()

d = [[-1]*w for _ in range(h)]
bfs(0,0)
if d[h-1][w-1] == -1: print(-1)
else:
  t = 0
  for i in range(h): t += s[i].count("#")
  print(h*w-t-(d[h-1][w-1]+1))