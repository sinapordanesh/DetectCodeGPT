def winner(N, K, A):
    dp = [False] * (K+1)
    for i in range(1, K+1):
        for a in A:
            if i - a >= 0 and not dp[i-a]:
                dp[i] = True
                break
    if dp[K]:
        return "First"
    else:
        return "Second"