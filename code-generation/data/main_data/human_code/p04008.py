from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, k = map(int, input().split())
a = [int(x)-1 for x in input().split()]
ans = 0
if a[0] != 0:
    ans += 1
    a[0] = 0


# g = [[] for _ in range(n)]
# for i in range(1, n):
#     g[i].append(a[i])
#     g[a[i]].append(i)


def dfs(v, par):
    global ans
    for w in g[v]:
        if w != par:
            dfs(w, v)
            if f[w]+1 == k and v != 0:
                ans += 1
                continue
            f[v] = max(f[v], f[w]+1)
    return ans


# TLE
# f = [0]*n
# print(dfs(0, -1))


# Topological Sort (TS)をDFSの代わりとする。
g = [[] for _ in range(n)]
indeg = [0]*n
for i in range(1, n):
    g[a[i]].append(i)
    indeg[i] += 1
q = deque([0])
TS = [0]
while q:
    v = q.popleft()
    for w in g[v]:
        indeg[w] -= 1
        if indeg[w] == 0:
            TS.append(w)
            q.append(w)

f = [0]*n
for w in TS[::-1]:
    if f[w] + 1 == k and a[w] != 0:
        ans += 1
        continue
    f[a[w]] = max(f[a[w]], f[w]+1)

print(ans)
