N = int(input())

tree = {}

for _ in range(N-1):
  A, B, C = [int(i) for i in input().split()]
  if A not in tree:
    tree[A] = []
  if B not in tree:
    tree[B] = []
  tree[A].append((B, C))
  tree[B].append((A, C))


c = {}
q = []
visited = set()

def dfs(a, acc):
  q.append((a, acc))

  while q:
    n, r = q.pop()
    c[n] = r
    visited.add(n)
    for b, cost in ((b, cost) for b, cost in tree[n] if b not in visited):
      q.append((b, cost + r))


Q, K = [int(i) for i in input().split()]
dfs(K, 0)

for _ in range(Q):
  x, y = [int(i) for i in input().split()]
  print(c[x] + c[y])
