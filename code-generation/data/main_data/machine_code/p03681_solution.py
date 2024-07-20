def count_arrangements(N, M):
    MOD = 10**9 + 7
    fact = [1] * (N + M + 1)
    for i in range(1, N + M + 1):
        fact[i] = fact[i-1] * i % MOD
        
    if abs(N - M) > 1:
        return 0
    elif N == M:
        return fact[N] * fact[M] * 2 % MOD
    else:
        return fact[N] * fact[M] % MOD

# Sample Input 1
print(count_arrangements(2, 2))

# Sample Input 2
print(count_arrangements(3, 2))

# Sample Input 3
print(count_arrangements(1, 8))

# Sample Input 4
print(count_arrangements(100000, 100000))