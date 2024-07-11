def main():
  N,M=map(int,input().split())

  if M == 0:
    print(-1)
    exit()

  INF = 10**6
  pqc = [tuple(map(lambda x:int(x)-1,input().split())) for _ in range(M)]

  to1d={v:{} for v in range(N)}
  count=2
  for p,q,c in pqc:
    if not to1d[p].get(c):
      to1d[p][c] = count
      count += 1
    if not to1d[q].get(c):
      to1d[q][c] = count
      count += 1

  G = [{} for _ in range(N+count)]
  for p,q,c in pqc:
    v1,v2 = to1d[p][c],to1d[q][c]
    G[v1][v2] = G[v2][v1] = 0

  for i in range(N):
    if len(to1d[i])<=1: continue
    for c in to1d[i].keys():
      v = to1d[i][c]
      G[v][count] = 1
      G[count][v] = 0
    count += 1

  def dijkstra(start = 0, goal = 1):
      from heapq import heappop, heappush
      NN = len(G)
      d = [INF]*NN
      d[start] = 0
      que = []
      heappush(que, start)
      while que:
          p = divmod(heappop(que),NN)
          v = p[1]
          if d[v] < p[0]: continue
          for u in G[v].keys():
              if d[u] > d[v] + G[v][u]:
                  d[u] = d[v] + G[v][u]
                  heappush(que, d[u]*NN+u)
          if v == goal: return d[goal]
      return d[goal]

  for c in to1d[0].keys():
    v = to1d[0][c]
    G[0][v] = 1
  for c in to1d[N-1].keys():
    v = to1d[N-1][c]
    G[v][1] = 0

  ans = dijkstra(0,1)
  print(ans if ans < INF else -1)
  
if __name__=="__main__":
  main()