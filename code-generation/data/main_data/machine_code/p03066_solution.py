def sequences(N, X):
    MOD = 998244353
    
    dp = [[0] * 3 for _ in range(X+1)]
    dp[0][0] = 1
    
    for i in range(1, N+1):
        new_dp = [[0] * 3 for _ in range(X+1)]
        for j in range(X+1):
            for k in range(3):
                for l in range(3):
                    if j+k == X:
                        continue
                    new_dp[j+k][(l+k)%3] = (new_dp[j+k][(l+k)%3] + dp[j][l]) % MOD
        dp = new_dp
        
    result = sum(dp[X])
    return result % MOD

N, X = map(int, input().split())
print(sequences(N, X))