import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M, S = mapint()
graph = [{} for _ in range(N)]
for _ in range(M):
    u, v, a, t = mapint()
    graph[u-1][v-1] = (a, t)
    graph[v-1][u-1] = (a, t)

change = [list(mapint()) for _ in range(N)]
from heapq import heappop, heappush
# time, silver, vertex
Q = [(0, min(2500, S), 0)]
dist = [[10**18]*2501 for _ in range(N)]
dist[0][min(2500, S)] = 0

while Q:
    t, s, v = heappop(Q)
    rate, change_time = change[v]
    if s<2500 and dist[v][min(2500, s+rate)]>t+change_time:
        dist[v][min(2500, s+rate)] = t+change_time
        heappush(Q, (t+change_time, min(2500, s+rate), v))
    for nx in graph[v].keys():
        nx_s, nx_t = graph[v][nx]
        if nx_s<=s and dist[nx][s-nx_s]>t+nx_t:
            dist[nx][s-nx_s] = t+nx_t
            heappush(Q, (t+nx_t, s-nx_s, nx))
for i in range(1, N):
    print(min(dist[i]))