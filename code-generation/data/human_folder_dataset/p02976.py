from collections import deque

def bfs():
    q = deque()
    q.append(1)
    dist[1] = 0
    while q:
        i = q.popleft()
        for g in G[i]:
            j, x = g[0], g[1]
            if dist[j] == -1:
                dist[j] = dist[i] + 1
                q.append(j)
                euse[x] = 1
                T[i].append([j, x])
                T[j].append([i, x])
                parent[j] = i
                v.append(j)
    return

n, m = map(int, input().split())
G = [[] for _ in range(n + 1)]
E = []
for i in range(m):
    a, b = map(int, input().split())
    G[a].append([b, i])
    G[b].append([a, i])
    E.append([a, b])
if m % 2 == 1:
    print(-1)
    exit()
T = [[] for _ in range(n + 1)]
euse = [0] * m
dist = [-1] * (n + 1)
parent = [0] * (n + 1)
v = deque()
bfs()
start = [0] * (n + 1)
for i in range(m):
    if not euse[i]:
        print(E[i][0], E[i][1])
        start[E[i][0]] += 1
while v:
    i = v.pop()
    for t in T[i]:
        if parent[i] == t[0]:
            j, x = t[0], t[1]
            break
    if start[i] % 2 == 0:
        start[j] += 1
        print(j, i)
    else:
        start[i] += 1
        print(i, j)