def num_strings(S, K):
    MOD = 998244353
    n = len(S)
    dp = [[0] * (K + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = 1
    
    for i in range(1, n + 1):
        for k in range(1, K + 1):
            for j in range(i):
                dp[i][k] += dp[j][k - 1]
                dp[i][k] %= MOD
    
    total_strings = sum(dp[i][K] for i in range(n + 1)) % MOD
    return total_strings

# Sample Input 1
print(num_strings("0101", 1))

# Sample Input 2
print(num_strings("01100110", 2))

# Sample Input 3
print(num_strings("1101010010101101110111100011011111011000111101110101010010101010101", 20))