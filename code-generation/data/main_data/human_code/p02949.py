n,m,p = map(int, input().split())
edge = []
inv_link = [[] for _ in range(n)]
link = [[] for _ in range(n)]

for i in range(m):
    a,b,cost = list(map(int,input().split()))
    edge.append([a-1,b-1,p-cost])
    link[a-1].append(b-1)
    inv_link[b-1].append(a-1)

def bell(edges, start,num_v):
    cost = [float('inf')] * num_v
    cost[start] = 0
    for _ in range(num_v):
        updated = False
        for a, b, c in edges:
            if cost[b] > cost[a] + c:
                cost[b] = cost[a] + c
                updated = True
        if not updated: break
    else:
        return False,cost
    return True,cost

from collections import deque
Q = deque()
Q.append([n-1,0])
visited=[-1]*n
visited[n-1]=0
while Q:
    now,cnt = Q.popleft()
    for nxt in inv_link[now]:
        if visited[nxt]!=-1:
            continue
        visited[nxt]=cnt+1
        Q.append([nxt,cnt+1])

new_edge=[]
for a,b,c in edge:
    if visited[a]==-1 or visited[b]==-1:
        continue
    new_edge.append([a,b,c])
ret,cost = bell(new_edge,0,n)
if ret:
    print(max(0,-cost[-1]))
else:
    print(-1)
