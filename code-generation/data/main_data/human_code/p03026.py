import sys
sys.setrecursionlimit(10000000)
n = int(input())
G = [[] for _ in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
c = list(map(int,input().split()))
c.sort()
node = [0]*n
used = [False]*n

def dfs(cur,point):
    used[cur] = True
    for nx in G[cur]:
        if used[nx]: continue
        t = c.pop()
        node[nx] = t
        point += min(node[cur],node[nx])
        point = dfs(nx,point)
    return point
node[0] = c.pop()
# print(dfs(0,-1,0))
print(dfs(0,0))
print(*node)