from collections import deque
 
N,u,v=map(int,input().split())
G=[[] for _ in range(N)]
for _ in range(N-1):
  a,b = map(int,input().split())
  G[a-1].append(b-1)
  G[b-1].append(a-1)
 
def bfs(s):
    seen = [0]*N
    d = [0]*N
    todo = deque()
    seen[s]=1
    todo.append(s)
    while len(todo):
      a = todo.popleft()
      for b in G[a]:
        if seen[b] == 0:
          seen[b] = 1
          todo.append(b)
          d[b] += d[a] + 1
    return d
  
d1 = bfs(u-1)
d2 = bfs(v-1)
 
print(max([d2[i] for i in range(N) if d1[i]<=d2[i]])-1)