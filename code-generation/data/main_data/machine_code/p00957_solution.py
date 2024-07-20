def chocolate_poles(l, k):
    dp = [[0] * (l + 1) for _ in range(2)]
    dp[0][0] = 1
    
    for i in range(1, k + 1):
        for j in range(l + 1):
            dp[i % 2][j] = dp[(i - 1) % 2][j]
            if j >= i:
                dp[i % 2][j] += dp[i % 2][j - i]
    
    return dp[k % 2][l]

# Test the function with the provided sample inputs
print(chocolate_poles(5, 3))
print(chocolate_poles(9, 10))
print(chocolate_poles(10, 10))
print(chocolate_poles(20, 5))
print(chocolate_poles(100, 2))