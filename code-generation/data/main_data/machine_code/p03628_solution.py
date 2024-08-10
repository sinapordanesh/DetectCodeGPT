def paint_dominoes(N, S1, S2):
    MOD = 1000000007
    dp = [0] * (N+1)
    dp[0] = 1
    
    for i in range(N):
        if S1[i] == S2[i]:
            dp[i+1] = dp[i]
        else:
            dp[i+1] = (2 * dp[i]) % MOD
    
    return dp[N]

# Sample Input 1
print(paint_dominoes(3, "aab", "ccb"))

# Sample Input 2
print(paint_dominoes(1, "Z", "Z"))

# Sample Input 3
print(paint_dominoes(52, "RvvttdWIyyPPQFFZZssffEEkkaSSDKqcibbeYrhAljCCGGJppHHn", "RLLwwdWIxxNNQUUXXVVMMooBBaggDKqcimmeYrhAljOOTTJuuzzn"))