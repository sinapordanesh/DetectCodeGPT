def count_pairs(N):
    MOD = 10**9 + 7
    return ((N + 1) * (N + 2) // 2) % MOD

N = int(input())
print(count_pairs(N))