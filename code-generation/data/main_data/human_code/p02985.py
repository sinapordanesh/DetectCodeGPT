# -*- coding: utf-8 -*-
# E - Virus Tree 2
import sys 
from collections import deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N, K = map(int, readline().split())
MOD = 10**9+7
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int,readline().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1]*(N+1)
dist[1] = K
q = deque([1])

def bfs():
    while q:
        x = q.popleft()
        if dist[x] == K:
            cnt = 1
        else:
            cnt = 2
        for nx in graph[x]:
            if dist[nx] != -1:
                continue
            dist[nx] = max(0,K-cnt)
            q.append(nx)
            cnt += 1
            
bfs()
ans = 1
for i in range(1,N+1):
    ans *= dist[i]
    ans %= MOD      
print(ans)