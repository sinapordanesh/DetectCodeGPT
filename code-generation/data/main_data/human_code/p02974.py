import sys
def input():
	return sys.stdin.readline()[:-1]
MOD = 10**9+7
n, K = map(int, input().split())
dp = [[[0 for _ in range(K+1)] for _ in range(n+1)] for _ in range(n+1)]
dp[0][0][0] = 1

for i in range(1, n+1):
	for j in range(n+1):
		for k in range(K+1):
			if k >= 2*j:
				dp[i][j][k] += (2*j+1) * dp[i-1][j][k-2*j]
			if k >= 2*j and j < n:
				dp[i][j][k] += (j+1) * (j+1) * dp[i-1][j+1][k-2*j]
			if k >= 2*j and j > 0:
				dp[i][j][k] += dp[i-1][j-1][k-2*j]
			dp[i][j][k] %= MOD

print(dp[n][0][K])