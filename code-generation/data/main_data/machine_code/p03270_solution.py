def combinations_of_sides(K, N):
    MOD = 998244353
    dp = [[0]*(N*K+1) for _ in range(N+1)]
    dp[0][0] = 1
    
    for i in range(1, N+1):
        for j in range(i*K+1):
            dp[i][j] = (dp[i][j] + dp[i-1][j]) % MOD
            if j >= K:
                dp[i][j] = (dp[i][j] - dp[i-1][j-K] + MOD) % MOD
    
    result = [0] * (2*K-1)
    for i in range(2, 2*K+1):
        for j in range(1, N+1):
            result[i-2] = (result[i-2] + dp[j][i]) % MOD
    
    return result

# Test the function with the sample inputs
print(*combinations_of_sides(3, 3))
print(*combinations_of_sides(4, 5))
print(*combinations_of_sides(6, 1000))