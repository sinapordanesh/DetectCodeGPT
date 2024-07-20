def divide_set(N, A, B, arr):
    MOD = 10**9 + 7
    
    dp = [0] * (N + 1)
    dp[0] = 1
    
    prefix_sum = [0] * (N + 1)
    
    left = 0
    for right in range(1, N + 1):
        while arr[right - 1] - arr[left] >= A:
            left += 1
        
        prefix_sum[right] = prefix_sum[right - 1] + dp[right - 1]
        
        if left > 0:
            dp[right] = (prefix_sum[right] - prefix_sum[left - 1]) % MOD
        else:
            dp[right] = prefix_sum[right] % MOD
    
    left = 0
    for right in range(1, N + 1):
        while arr[right - 1] - arr[left] >= B:
            left += 1
        
        prefix_sum[right] = prefix_sum[right - 1] + dp[right - 1]
        
        if left > 0:
            dp[right] = (prefix_sum[right] - prefix_sum[left - 1]) % MOD
        else:
            dp[right] = prefix_sum[right] % MOD
    
    return dp[-1]

# Sample Input
print(divide_set(5, 3, 7, [1, 3, 6, 9, 12]))
print(divide_set(7, 5, 3, [0, 2, 4, 7, 8, 11, 15]))
print(divide_set(8, 2, 9, [3, 4, 5, 13, 15, 22, 26, 32]))
print(divide_set(3, 3, 4, [5, 6, 7]))