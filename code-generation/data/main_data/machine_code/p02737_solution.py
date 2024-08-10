def max_weight_independent_set():
    MOD = 998244353
    N = int(input())
    X = [[] for _ in range(N)]
    Y = [[] for _ in range(N)]
    Z = [[] for _ in range(N)]
    
    M1 = int(input())
    for _ in range(M1):
        a, b = map(int, input().split())
        X[a-1].append(b-1)
        X[b-1].append(a-1)
    
    M2 = int(input())
    for _ in range(M2):
        c, d = map(int, input().split())
        Y[c-1].append(d-1)
        Y[d-1].append(c-1)
    
    M3 = int(input())
    for _ in range(M3):
        e, f = map(int, input().split())
        Z[e-1].append(f-1)
        Z[f-1].append(e-1)
    
    dp = [[0, 0] for _ in range(N)] # dp[i][0] is the max weight not including vertex i, dp[i][1] is the max weight including vertex i
    
    for _ in range(N):
        dp[_][0] = dp[_][1] = 1
    
    for i in range(N):
        for j in X[i]:
            dp[i][0] = (dp[i][0] * (dp[j][0] + dp[j][1])) % MOD
            dp[i][1] = (dp[i][1] * dp[j][0]) % MOD
    
    for i in range(N):
        for j in Y[i]:
            dp[i][0] = (dp[i][0] * (dp[j][0] + dp[j][1])) % MOD
            dp[i][1] = (dp[i][1] * dp[j][0]) % MOD
    
    for i in range(N):
        for j in Z[i]:
            dp[i][0] = (dp[i][0] * (dp[j][0] + dp[j][1])) % MOD
            dp[i][1] = (dp[i][1] * dp[j][0]) % MOD
    
    result = sum(dp[i][0] for i in range(N)) % MOD
    print(result)

max_weight_independent_set()