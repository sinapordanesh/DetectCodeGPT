from collections import deque
from itertools import product


def bfs():
    while q:
        i, j = q.popleft()
        for di, dj in (1, 0), (-1, 0), (0, 1), (0, -1):
            ni, nj = i + di, j + dj
            if not (0 <= ni < H and 0 <= nj < W and dist[ni][nj] < 0):
                continue
            dist[ni][nj] = dist[i][j] + 1
            q.append((ni, nj))


H, W = map(int, input().split())
A = [input() for _ in range(H)]

q = deque()
dist = [[-1] * W for _ in range(H)]
for i, j in product(range(H), range(W)):
    if A[i][j] == ".":
        continue
    q.append((i, j))
    dist[i][j] = 0
bfs()
print(max(max(row) for row in dist))