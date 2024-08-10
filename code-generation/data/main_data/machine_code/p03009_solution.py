def ways_to_stack_blocks(N, H, D):
    MOD = 10**9 + 7
    dp = [0] * (H + 1)
    dp[0] = 1
    
    for i in range(1, H + 1):
        dp[i] = dp[i-1]
        if i - D >= 0:
            dp[i] += dp[i-D]
        dp[i] %= MOD
    
    return pow(dp[H], N, MOD)

N, H, D = map(int, input().split())
print(ways_to_stack_blocks(N, H, D))