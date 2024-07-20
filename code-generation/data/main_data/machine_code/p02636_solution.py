def count_strings(S):
    MOD = 998244353
    n = len(S)
    dp = [0] * (n+1)
    dp[0] = 1
    
    for i in range(1, n+1):
        dp[i] = (dp[i-1] * 2) % MOD
        for j in range(2, i+1):
            if S[i-j] == S[i-1]:
                dp[i] = (dp[i] + dp[i-j]) % MOD
    
    return dp[n]

S = input().strip()
print(count_strings(S))