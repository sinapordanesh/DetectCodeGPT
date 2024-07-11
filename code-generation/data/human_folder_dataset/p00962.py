from heapq import heappush, heappop
from collections import deque
import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
E = []
G = [[] for i in range(n)]
RG = [[] for i in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    E.append((a-1, b-1, c))
    G[a-1].append((b-1, c, i))
    RG[b-1].append((a-1, c, i))
def dijkstra(G, s):
    dist = [10**18]*n
    dist[s] = 0
    que = [(0, s)]
    while que:
        co, v = heappop(que)
        if dist[v] < co:
            continue
        for w, c, i in G[v]:
            if co + c < dist[w]:
                dist[w] = co + c
                heappush(que, (co + c, w))
    return dist
D = dijkstra(G, 0)
RD = dijkstra(RG, 1)

G0 = [[] for i in range(n)]
used = set([1])
deq = deque([1])
P = set()
while deq:
    v = deq.popleft()
    for w, c, i in RG[v]:
        if D[w] + c == D[v]:
            P.add(i)
            if w not in used:
                used.add(w)
                deq.append(w)
            G0[v].append((w, i))
            G0[w].append((v, i))

PB = set()
label = [None]*n
gen = 1
cost = [0]*n
def dfs(u, p, i):
    global gen
    res = 0
    p_cnt = 0
    for v, j in G0[u]:
        if v == p:
            p_cnt += 1
            continue
        if label[v] is not None:
            if label[v] < label[u]:
                cost[v] += 1
                res += 1
        else:
            label[v] = gen; gen += 1
            res += dfs(v, u, j)
    res -= cost[u]
    if res == 0 and p != -1 and p_cnt == 1:
        PB.add(i)
    return res
label[0] = 0
dfs(0, -1, None)

ans = []
for i in range(m):
    if i in P:
        if i in PB:
            ans.append("SAD")
        else:
            ans.append("SOSO")
    else:
        a, b, c = E[i]
        if D[b] + c + RD[a] < D[1]:
            ans.append("HAPPY")
        else:
            ans.append("SOSO")
print(*ans, sep='\n')