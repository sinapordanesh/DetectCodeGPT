def count_valid_strings(N):
    MOD = 10**9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1
    
    for i in range(1, N + 1):
        dp[i] = (dp[i-1] * 3) % MOD
    
    for i in range(2, N + 1):
        dp[i] = (dp[i] + dp[i-2] * 2) % MOD
    
    for i in range(3, N + 1):
        dp[i] = (dp[i] + dp[i-3]) % MOD
    
    invalid = 0
    invalid += dp[N]
    for i in range(1, N):
        invalid += dp[i] * dp[N-i]
    invalid %= MOD
    
    return (dp[N] ** 4 - invalid) % MOD

# Test the function with sample inputs
print(count_valid_strings(3))
print(count_valid_strings(4))
print(count_valid_strings(100))