def max_length_sequence(N, K, A):
    dp = [0] * N
    for i in range(N):
        dp[i] = 1
        for j in range(i):
            if abs(A[i] - A[j]) <= K:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)