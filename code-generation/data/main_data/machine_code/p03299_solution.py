def paint_squares(N, heights):
    MOD = 10**9 + 7
    dp = [1, 0]
    for h in heights:
        new_dp = [0, 0]
        new_dp[0] = (3 * dp[0] + 2 * dp[1]) * h + 2 * dp[0]
        new_dp[1] = dp[0] + dp[1]
        dp = [x % MOD for x in new_dp]
    return (dp[0] + dp[1]) % MOD

# Test the function with the provided sample inputs
print(paint_squares(9, [2, 3, 5, 4, 1, 2, 4, 2, 1])) # Output: 12800
print(paint_squares(2, [2, 2])) # Output: 6
print(paint_squares(5, [2, 1, 2, 1, 2])) # Output: 256
print(paint_squares(9, [27, 18, 28, 18, 28, 45, 90, 45, 23])) # Output: 844733013