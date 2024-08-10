def subset_sum(N, S, A):
    mod = 998244353
    dp = [0] * (S+1)
    dp[0] = 1
    
    for a in A:
        for i in range(S,a-1,-1):
            dp[i] += dp[i-a]
            dp[i] %= mod
    
    result = sum(dp) - 1
    return result % mod

# Sample Input 1
print(subset_sum(3, 4, [2, 2, 4]))

# Sample Input 2
print(subset_sum(5, 8, [9, 9, 9, 9, 9]))

# Sample Input 3
print(subset_sum(10, 10, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))