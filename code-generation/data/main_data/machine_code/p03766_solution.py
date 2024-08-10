MOD = 10**9 + 7

def count_sequences(n):
    dp = [1] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = (dp[i - 1] * (n + 1 - i)) % MOD
    return dp[n]

n = int(input())
print(count_sequences(n))