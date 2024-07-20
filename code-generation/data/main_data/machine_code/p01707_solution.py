def count_ways(N, D, X):
    MOD = 100000007
    dp = [[0] * (N + 1) for _ in range(D + 1)]
    dp[0][0] = 1
    for d in range(1, D + 1):
        for n in range(N + 1):
            for x in range(1, X):
                if n - x >= 0:
                    dp[d][n] += dp[d - 1][n - x]
                    dp[d][n] %= MOD
    return dp[D][N]

while True:
    N, D, X = map(int, input().split())
    if N == 0 and D == 0 and X == 0:
        break
    print(count_ways(N, D, X))