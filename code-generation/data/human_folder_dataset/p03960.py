import sys
input = sys.stdin.readline
INF = 10**10
h, w = map(int, input().split())
C = [input().rstrip() for _ in range(h)]
def solve(b):
  cost = [[0]*(h+1) for _ in range(h+1)]
  dp = [[INF]*(h+1) for _ in range(h+1)]
  dp[0][0] = 0
  for i in range(h+1):
    for j in range(h+1):
      if i and j:
        cost[i][j] = cost[i-1][j-1] - (C[h-i][b] == C[h-j][b+1])
      else:
        for r in range(min(h-i, h-j)):
          cost[i][j] += C[j+r][b] == C[i+r][b+1]
      if i:
        dp[i][j] = min(dp[i][j], dp[i-1][j]+cost[i-1][j])
      if j:
        dp[i][j] = min(dp[i][j], dp[i][j-1]+cost[i][j-1])
  return dp[h][h]
ans = 0
for b in range(w-1):
  ans += solve(b)
print(ans)