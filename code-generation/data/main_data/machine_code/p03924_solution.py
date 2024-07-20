MOD = 10**9 + 7

def count_sequences(N, M):
    dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(M + 1)]
    
    for i in range(1, N + 1):
        dp[1][i][i] = 1
    
    for i in range(1, M):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                for l in range(1, N + 1):
                    if k != l:
                        dp[i + 1][j][l] = (dp[i + 1][j][l] + dp[i][j][k]) % MOD
    
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            ans = (ans + dp[M][i][j]) % MOD
    
    return ans

# Sample Input 1
N = 3
M = 3
print(count_sequences(N, M))

# Sample Input 2
N = 150
M = 300
print(count_sequences(N, M))

# Sample Input 3
N = 300
M = 150
print(count_sequences(N, M))