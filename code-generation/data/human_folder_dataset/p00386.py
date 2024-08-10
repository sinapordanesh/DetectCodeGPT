import sys
sys.setrecursionlimit(1000000)
def main():
  n, q = map(int, input().split())
  edges = [[] for _ in range(n)]
  for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append((v, w))
    edges[v].append((u, w))
  
  height = [None] * n
  dist = [None] * n
  parent = [[None] * 20 for _ in range(n)]
  stack = [(0, 0, 0)]
  while stack:
    x, h, d = stack.pop()
    height[x] = h
    dist[x] = d
    for to, w in edges[x]:
      if height[to] == None:
        parent[to][0] = x
        stack.append((to, h + 1, d + w))
  for j in range(1, 20):
    for i in range(1, n):
      if height[i] >= 2 ** j:
        parent[i][j] = parent[parent[i][j - 1]][j - 1]
  
  def adj_height(x, n):
    if n == 0:
      return x
    acc = 1
    for i in range(20):
      if acc > n:
        return adj_height(parent[x][i - 1], n - acc // 2)
      acc *= 2
  
  def _lca(x, y):
    if x == y:
      return x
    for i in range(1 ,20):
      if parent[x][i] == parent[y][i]:
        return _lca(parent[x][i - 1], parent[y][i - 1])
  
  def lca(x, y):
    diff = height[x] - height[y]
    if diff < 0:
      y = adj_height(y, -diff)
    elif diff > 0:
      x = adj_height(x, diff)
    return _lca(x, y)
  
  def bs(index, target):
    if index == 0:
      return 0
    if dist[index] >= target >= dist[parent[index][0]]:
      return index
    for i in range(1, 20):
      if parent[index][i] == None or dist[parent[index][i]] <= target:
        return bs(parent[index][i - 1], target)
  
  def max_dist(x, y, z, r):
    xr = lca(x, r)
    yr = lca(y, r)
    zr = lca(z, r)
    return max(dist[x] + dist[r] - dist[xr] * 2, 
               dist[y] + dist[r] - dist[yr] * 2,
               dist[z] + dist[r] - dist[zr] * 2)
  
  def _score(x, y, z, xy, yz):
    dist_x = dist[x]
    dist_y = dist[y]
    dist_z = dist[z]
    dist_xy = dist[xy]
    dist_yz = dist[yz]
    dx = dist_x + dist_yz - dist_xy * 2
    dy = dist_y - dist_yz
    dz = dist_z - dist_yz
    if dx >= dy >= dz:
      if dist_x >= dist_y:
        r = bs(x, dist_xy + (dist_x - dist_y) / 2)
        if r == 0:
          return dist_x
        return min(max(dist_x - dist[r], dist_y + dist[r] - dist_xy * 2), 
                   max(dist_x - dist[parent[r][0]], dist_y + dist[parent[r][0]] - dist_xy * 2))
      else:
        r = bs(yz, dist_xy + (dist_y - dist_x) / 2)
        if r == 0:
          return dist_y
        return min(max(dist_y - dist[r], dist_x + dist[r] - dist_xy * 2), 
                   max(dist_y - dist[parent[r][0]], dist_x + dist[parent[r][0]] - dist_xy * 2))
  
    elif dx >= dz >= dy:
      if dist_x >= dist_z:
        r = bs(x, dist_xy + (dist_x - dist_z) / 2)
        if r == 0:
          return dist_x
        return min(max(dist_x - dist[r], dist_z + dist[r] - dist_xy * 2), 
                   max(dist_x - dist[parent[r][0]], dist_z + dist[parent[r][0]] - dist_xy * 2))
      else:
        r = bs(yz, dist_xy + (dist_z - dist_x) / 2)
        if r == 0:
          return dist_z
        return min(max(dist_z - dist[r], dist_x + dist[r] - dist_xy * 2), 
                   max(dist_z - dist[parent[r][0]], dist_x + dist[parent[r][0]] - dist_xy * 2))
 
    elif dy >= dx >= dz:
      r = bs(y, dist_yz + (dy - dx) / 2)
      if r == 0:
        return dist_y
      return min(max(dist_y - dist[r], dist_x + dist[r] - dist_xy * 2), 
                 max(dist_y - dist[parent[r][0]], dist_x + dist[parent[r][0]] - dist_xy * 2))
 
    elif dy >= dz >= dx:
      r = bs(y, dist_yz + (dy - dz) / 2)
      if r == 0:
        return dist_y
      return min(max(dist_y - dist[r], dist_z + dist[r] - dist_yz * 2), 
                 max(dist_y - dist[parent[r][0]], dist_z + dist[parent[r][0]] - dist_yz * 2))
 
    elif dz >= dx >= dy:
      r = bs(z, dist_yz + (dz - dx) / 2)
      if r == 0:
        return dist_z
      return min(max(dist_z - dist[r], dist_x + dist[r] - dist_xy * 2), 
                 max(dist_z - dist[parent[r][0]], dist_x + dist[parent[r][0]] - dist_xy * 2))
 
    elif dz >= dy >= dx:
      r = bs(z, dist_yz + (dz - dy) / 2)
      if r == 0:
        return dist_z
      return min(max(dist_z - dist[r], dist_y + dist[r] - dist_yz * 2), 
                 max(dist_z - dist[parent[r][0]], dist_y + dist[parent[r][0]] - dist_yz * 2))
  
  def score(a, b, c):
    a -= 1
    b -= 1
    c -= 1
    ab = lca(a, b)
    ac = lca(a, c)
    bc = lca(b, c)
    if ab == ac:
      return _score(a, b, c, ab, bc)
    elif ab == bc:
      return _score(b, a, c, ab, ac)
    else:
      return _score(c, a, b, ac, ab)
  
  for _ in range(q):
    a, b, c = map(int, input().split())
    print(score(a, b, c))

main()
