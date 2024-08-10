def max_sum_beauties(N, heights, beauties):
    dp = [0] * N
    for i in range(N):
        dp[i] = beauties[i]
        for j in range(i):
            if heights[i] > heights[j]:
                dp[i] = max(dp[i], dp[j] + beauties[i])
    return max(dp)