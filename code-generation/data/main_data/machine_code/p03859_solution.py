def possible_values_after_operations(N, M, S, operations):
    MOD = 1000000007
    
    dp = [[0] * (N+1) for _ in range(M+1)]
    dp[0][0] = 1
    
    for i in range(1, M+1):
        acc = [0] * (N+1)
        for j in range(N):
            acc[j+1] = (acc[j] + dp[i-1][j]) % MOD
        
        l = operations[i-1][0] - 1
        r = operations[i-1][1] - 1
        
        for j in range(N):
            if j < l:
                dp[i][j] = acc[j+1]
            else:
                dp[i][j] = (acc[j+1] - acc[l] + dp[i-1][l] + MOD) % MOD
            if j + 1 <= r:
                dp[i][j] = (dp[i][j] + dp[i][j-1]) % MOD
    
    return sum(dp[-1]) % MOD

# Sample Input
print(possible_values_after_operations(5, 2, '01001', [(2, 4), (3, 5)]))
print(possible_values_after_operations(9, 3, '110111110', [(1, 4), (4, 6), (6, 9)]))
print(possible_values_after_operations(11, 6, '00101000110', [(2, 4), (2, 3), (4, 7), (5, 6), (6, 10), (10, 11)]))