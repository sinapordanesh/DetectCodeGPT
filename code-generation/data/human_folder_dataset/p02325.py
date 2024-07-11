import sys
sys.setrecursionlimit(1000000)

def calc(p1, p2, v):
    dists_v = dists[v]
    if v == n - 1:
        return dists_v[p1] + dists_v[p2]
    if visited[p1][p2]:
        return dp[p1][p2]
    dp[p1][p2] = min(dists_v[p1] + calc(p2, v, v + 1), dists_v[p2] + calc(p1, v, v + 1))
    visited[p1][p2] = True
    return dp[p1][p2]


n = int(input())
points = [complex(*map(int, input().split())) for _ in range(n)]
dists = [[abs(p1 - p2) for p2 in points] for p1 in points]
visited = [[False] * n for _ in range(n)]
dp = [[0] * n for _ in range(n)]

print(calc(0, 0, 0))