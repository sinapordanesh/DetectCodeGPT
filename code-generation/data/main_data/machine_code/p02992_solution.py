MOD = 10**9 + 7

def count_sequences(N, K):
    dp = [[0] * (N+1) for _ in range(K)]
    
    for i in range(1, N+1):
        dp[0][i] = 1
    
    for i in range(1, K):
        for j in range(1, N+1):
            dp[i][j] = sum(dp[i-1][x] for x in range(1, j+1))
    
    return sum(dp[-1]) % MOD

N, K = map(int, input().split())
print(count_sequences(N, K))