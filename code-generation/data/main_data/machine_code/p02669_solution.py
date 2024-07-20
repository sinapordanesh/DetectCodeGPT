def min_coins(T, testcases):
    result = []
    
    for i in range(T):
        N, A, B, C, D = testcases[i]
        dp = [float('inf')] * (N + 1)
        dp[0] = 0
        
        for j in range(1, N + 1):
            dp[j] = min(dp[j], dp[j - 1] + D)
            if j % 2 == 0:
                dp[j] = min(dp[j], dp[j // 2] + A)
            if j % 3 == 0:
                dp[j] = min(dp[j], dp[j // 3] + B)
            if j % 5 == 0:
                dp[j] = min(dp[j], dp[j // 5] + C)
        
        result.append(dp[N])
    
    return result

# Sample Input
T = 5
testcases = [(11, 1, 2, 4, 8), (11, 1, 2, 2, 8), (32, 10, 8, 5, 4), (29384293847243, 454353412, 332423423, 934923490, 1), (900000000000000000, 332423423, 454353412, 934923490, 987654321)]

# Calling the function
min_coins(T, testcases)