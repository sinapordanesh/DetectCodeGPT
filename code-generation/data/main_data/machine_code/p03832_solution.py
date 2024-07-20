import sys

MOD = 10**9 + 7

def count_ways_to_divide_people():
    N, A, B, C, D = map(int, input().split())
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(A, B + 1):
                if i - k >= 0:
                    for l in range(C, D + 1):
                        if j - l >= 0:
                            dp[i][j] += dp[i - k][j - l]
                            dp[i][j] %= MOD

    print(dp[N][N])

count_ways_to_divide_people()