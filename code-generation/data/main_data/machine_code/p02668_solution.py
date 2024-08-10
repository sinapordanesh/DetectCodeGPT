MOD = 10**9 + 7

def count_sequences(N, M):
    dp = [[0] * (1 << N) for _ in range(M+1)]
    dp[0][0] = 1
    
    for i in range(1, M+1):
        for j in range(1 << N):
            for k in range(1 << N):
                if bin(j ^ k).count('1') % 2 == 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
    
    return sum(dp[M]) % MOD

N, M = map(int, input().split())
print(count_sequences(N, M))