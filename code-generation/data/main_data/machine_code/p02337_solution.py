MOD = 10**9 + 7

def put_balls_in_boxes(n, k):
    dp = [[0] * (k+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] * j) % MOD
    return dp[n][k]

n, k = map(int, input().split())
print(put_balls_in_boxes(n, k))