def count_states(N, M, A, B, C, D):
    MOD = 998244353
    
    dp = [[0] * 4 for _ in range(N+1)]
    dp[0][0] = dp[0][1] = dp[0][2] = dp[0][3] = 1
    
    for i in range(1, N+1):
        dp[i][0] = (dp[i-1][1] + dp[i-1][2] + dp[i-1][3]) % MOD
        dp[i][1] = (dp[i-1][0] + dp[i-1][2] + dp[i-1][3]) % MOD
    
    dp2 = [[0] * 4 for _ in range(M+1)]
    dp2[0][0] = dp2[0][1] = dp2[0][2] = dp2[0][3] = 1
    
    for i in range(1, M+1):
        dp2[i][2] = (dp2[i-1][1] + dp2[i-1][0] + dp2[i-1][3]) % MOD
        dp2[i][3] = (dp2[i-1][0] + dp2[i-1][1] + dp2[i-1][2]) % MOD
    
    res = 1
    for a in A:
        res *= dp[N][int(a)]
        res %= MOD
    
    for b in B:
        res *= dp[N][int(b)]
        res %= MOD
    
    for c in C:
        res *= dp2[M][int(c)]
        res %= MOD
    
    for d in D:
        res *= dp2[M][int(d)]
        res %= MOD
    
    return res

# Sample Input 1
print(count_states(2, 2, "10", "01", "10", "01")) # 6

# Sample Input 2
print(count_states(2, 2, "11", "11", "11", "11")) # 32

# Sample Input 3
print(count_states(3, 4, "111", "111", "1111", "1111")) # 1276

# Sample Input 4
print(count_states(17, 21, "11001010101011101", "11001010011010111", "111010101110101111100", "011010110110101000111")) # 548356548

# Sample Input 5
print(count_states(3, 4, "000", "101", "1111", "0010")) # 21

# Sample Input 6
print(count_states(9, 13, "111100001", "010101011", "0000000000000", "1010111111101")) # 177856

# Sample Input 7
print(count_states(23, 30, "01010010101010010001110", "11010100100100101010101", "000101001001010010101010101101", "101001000100101001010010101000")) # 734524988