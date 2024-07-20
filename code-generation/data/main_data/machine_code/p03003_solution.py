
def count_pairs(N, M, S, T):
    MOD = 10**9 + 7
    
    dp = [[0] * (M+1) for _ in range(N+1)]
    
    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j] = (2*dp[i-1][j] + 2*dp[i][j-1] - dp[i-1][j-1] + (S[i-1]==T[j-1])) % MOD
    
    return dp[N][M] % MOD

# Input
N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

# Output
print(count_pairs(N, M, S, T))