import copy, sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
A = [int(i) for i in input().split()]
edge = [[] for i in range(n)]

grundy = [-1] * n

for i in range(n-1):
    a, b = [int(i) for i in input().split()]
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

def dfs(v):
    if grundy[v] != -1: return grundy[v]
    mex = [0] * (len(edge[v]) + 1)
    for vv in edge[v]:
        if A[vv] < A[v]: 
            gg = dfs(vv)
            if gg <= len(edge[v]): mex[gg] = 1
    for i in range(len(edge[v])+1):
        if mex[i] == 0:
            grundy[v] = i
            return i

for i in range(n):
    dfs(i)

ans = []
for i in range(n):
    if grundy[i] != 0: ans.append(i+1)

print(*ans)
