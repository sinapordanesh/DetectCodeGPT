def count_pairs(L):
    MOD = 10**9 + 7
    count = 0
    for i in range(32):
        if L & (1 << i):
            count += pow(2, i, MOD)
            count %= MOD
    return (L + 1) * (L + 2) // 2 - 2 * count % MOD

L = 10
print(count_pairs(L))