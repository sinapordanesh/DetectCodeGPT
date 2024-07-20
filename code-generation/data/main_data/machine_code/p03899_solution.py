def max_total_score(N, M, K, A):
    dp = [0] * (N + 1)
    for i in range(1, K + 1):
        new_dp = [0] * (N + 1)
        for j in range(1, N + 1):
            new_dp[j] = max(dp[j], dp[max(0, j - M)] + i * A[j - 1])
        dp = new_dp
    return max(dp)