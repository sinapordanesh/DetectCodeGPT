def count_pairs(N, M):
    MOD = 10**9 + 7
    ans = 1
    for i in range(1, N+1):
        ans = (ans * i) % MOD
    for i in range(1, M+1):
        ans = (ans * i) % MOD
    for i in range(1, N*2+1):
        ans = (ans * pow(i, MOD-2, MOD)) % MOD
    return ans

# Sample Input 1
print(count_pairs(2, 2))

# Sample Input 2
print(count_pairs(2, 3))

# Sample Input 3
print(count_pairs(141421, 356237))