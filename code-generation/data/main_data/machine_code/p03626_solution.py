def paint_dominoes(N, S1, S2):
    MOD = 1000000007
    dp = [0] * (N+1)
    dp[0] = 1
    
    for i in range(N):
        if S1[i] == S2[i]:
            dp[i+1] = dp[i] * 3 % MOD
        else:
            dp[i+1] = dp[i] * 2 % MOD
    
    return dp[N]

N = 52
S1 = "RvvttdWIyyPPQFFZZssffEEkkaSSDKqcibbeYrhAljCCGGJppHHn"
S2 = "RLLwwdWIxxNNQUUXXVVMMooBBaggDKqcimmeYrhAljOOTTJuuzzn"
print(paint_dominoes(N, S1, S2))