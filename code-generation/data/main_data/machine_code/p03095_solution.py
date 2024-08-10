def count_unique_subsequences(N, S):
    mod = 10**9 + 7
    dp = [0] * (N + 1)
    last = {}
    dp[0] = 1
    for i in range(1, N + 1):
        dp[i] = dp[i - 1] * 2 % mod
        if S[i - 1] in last:
            dp[i] -= dp[last[S[i - 1]] - 1]
        dp[i] %= mod
        last[S[i - 1]] = i
    return (dp[N] - 1) % mod

N = int(input())
S = input().strip()
print(count_unique_subsequences(N, S))