def expected_number_of_operations(N, A):
    MOD = 998244353
    
    S = sum(A)
    
    dp = [0] * (1 << N)
    dp[0] = 1
    
    for _ in range(S):
        ndp = [0] * (1 << N)
        s = 0
        
        for i in range(1 << N):
            s += dp[i]
            s %= MOD
        
        for i in range(1 << N):
            for j in range(N):
                v = i ^ (1 << j)
                ndp[v] += dp[i] * A[v] % MOD * pow(s, MOD - 2, MOD) % MOD
                ndp[v] %= MOD
        
        dp = ndp
    
    for ans in dp:
        print(ans)

# Sample Input 1
N = 2
A = [1, 1, 1, 1]
expected_number_of_operations(N, A)

# Sample Input 2
N = 2
A = [1, 2, 1, 2]
expected_number_of_operations(N, A)

# Sample Input 3
N = 4
A = [337, 780, 799, 10, 796, 875, 331, 223, 941, 67, 148, 483, 390, 565, 116, 355]
expected_number_of_operations(N, A)