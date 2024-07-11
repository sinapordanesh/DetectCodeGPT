INF = 10 ** 20

def search(rest, now, goal, dp, edges):
  if now == goal:
    return 0
  if rest == ():
    if now == goal:
      return 0
    else:
      return INF

  if (rest, now) in dp:
    return dp[(rest, now)]

  ret = INF
  for i, t in enumerate(rest):
    for dist, to in edges[now]:
      ret = min(ret, search(tuple(v for j, v in enumerate(rest) if i != j), to, goal, dp, edges) + dist / t)
  dp[(rest, now)] = ret
  return ret

while True:
  n, m, p, a, b = map(int, input().split())
  if n == 0:
    break
  a -= 1
  b -= 1
  tlst = list(map(int, input().split()))
  edges = [[] for _ in range(m)]
  for _ in range(p):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    edges[x].append((z, y))
    edges[y].append((z, x))
  tlst.sort()
  rest = tuple(tlst)
  dp = {}
  ans = search(rest, a, b, dp, edges)
  if ans == INF:
    print("Impossible")
  else:
    print(ans)
 
