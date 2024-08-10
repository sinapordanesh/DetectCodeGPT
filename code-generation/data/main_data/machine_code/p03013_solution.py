def climb_stairs(N, M, broken_steps):
    MOD = 1000000007
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1, N+1):
        if i not in broken_steps:
            dp[i] = (dp[i-1] + dp[i-2]) % MOD
    return dp[N]

# Sample Input 1
print(climb_stairs(6, 1, [3])) # Output: 4

# Sample Input 2
print(climb_stairs(10, 2, [4, 5])) # Output: 0

# Sample Input 3
print(climb_stairs(100, 5, [1, 23, 45, 67, 89])) # Output: 608200469