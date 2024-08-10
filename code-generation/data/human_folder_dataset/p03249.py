import sys
sys.setrecursionlimit(10**7)
n = int(input())
d = [int(input()) for _ in range(n)]
r = {v: i for i, v in enumerate(d)}
sz = [1] * n
dsorted = sorted(((di, i) for i, di in enumerate(d)), reverse=True)
ans = []
to = [[] for _ in range(n)]
for di, i in dsorted[:n-1]:
    nd = di + (sz[i] - 1) - (n - 2 - (sz[i] - 1))
    if not nd in r:
        print(-1)
        exit()
    p = r[nd]
    to[p].append(i)
    sz[p] += sz[i]
    ans.append((i+1, p+1))

root = dsorted[-1][1]
def dfs(u, cur=0):
    rv = cur
    for v in to[u]:
        rv += dfs(v, cur + 1)
    return rv

if dfs(root) != d[root]:
    print(-1)
    exit()

for u, v in ans:
    print(u, v)
