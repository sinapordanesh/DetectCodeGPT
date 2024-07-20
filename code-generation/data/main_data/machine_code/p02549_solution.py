def number_of_ways(N, K, segments):
    MOD = 998244353
    dp = [0] * N
    dp[0] = 1
    
    for i in range(1, N):
        for l, r in segments:
            dp[i] += dp[max(i-l, 0)] - dp[max(i-r-1, 0)]
            dp[i] %= MOD
    
    return dp[N-1] % MOD

# Sample Input 1
print(number_of_ways(5, 2, [(1, 1), (3, 4)]))

# Sample Input 2
print(number_of_ways(5, 2, [(3, 3), (5, 5)]))

# Sample Input 3
print(number_of_ways(5, 1, [(1, 2)]))

# Sample Input 4
print(number_of_ways(60, 3, [(5, 8), (1, 3), (10, 15)]))