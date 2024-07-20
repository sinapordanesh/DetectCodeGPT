import sys
from collections import deque

input = sys.stdin.buffer.readline
sys.setrecursionlimit(2*10**5)

N = int(input())
c = list(map(int,input().split()))
edge = [[] for i in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)


#合流点の検出
deq = deque([1])
parent = [-1 for i in range(N+1)]
parent[1] = 0
topo = []
while deq:
    v = deq.popleft()
    topo.append(v)
    for nv in edge[v]:
        if parent[nv]==-1:
            parent[nv] = v
            deq.append(nv)

topo = topo[::-1]


#辺の張り直し
vertex = []
size = [1 for i in range(N+1)]
size[0] = N

def euler_tour(v,pv):
    vertex.append(v)
    for nv in edge[v]:
        if nv!=pv:
            euler_tour(nv,v)
            size[v] += size[nv]
    vertex.append(v)
euler_tour(1,0)

color_tree_edge = [{c[i]:[]} for i in range(N)]
color_tree_edge = [{c:[] for c in range(1,N+1)}] + color_tree_edge
for v in range(2,N+1):
    color_tree_edge[v][c[parent[v]-1]] = []

parent = [0 for i in range(N+1)]
visit = [None for i in range(N+1)]

for v in vertex:
    if visit[v] is None:
        visit[v] = {}
        for nc in color_tree_edge[v]:
            color_tree_edge[parent[nc]][nc].append(v)
            visit[v][nc] = parent[nc]
            parent[nc] = v
    else:
        for nc in visit[v]:
            parent[nc] = visit[v][nc]

def bfs(color):
    deq = deque([0])
    res = []
    while deq:
        v = deq.popleft()
        res.append(v)
        for nv in color_tree_edge[v][color]:
            deq.append(nv)

    return res[::-1]

ans = [0]*(N+1)

for color in range(1,N+1):
    vertex = bfs(color)
    res = N*(N+1)//2
    for v in vertex:
        if v==0 or c[v-1]!=color:
            tmp = size[v]
            for nv in color_tree_edge[v][color]:
                tmp -= size[nv]
            res -= tmp*(tmp+1)//2
    ans[color] = res

print("\n".join(map(str,ans[1:])))
