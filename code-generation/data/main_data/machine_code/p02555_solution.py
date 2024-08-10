def count_sequences(S):
    MOD = 10**9 + 7
    dp = [0] * (S + 1)
    dp[0] = 1
    for i in range(3, S + 1):
        dp[i] = dp[i-3] + dp[i-1] % MOD
    return dp[S] % MOD

S = int(input())
print(count_sequences(S))