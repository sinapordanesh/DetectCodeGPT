import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())
if n % 2:exit(print("First"))
edges = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)
def dfs(v, prev):
    res = sum(dfs(u, v) for u in edges[v] if u != prev)
    if res >= 2:exit(print("First"))
    return not res
print("First" if dfs(0, -float("inf")) else "Second")