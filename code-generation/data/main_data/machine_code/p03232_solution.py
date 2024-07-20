def total_cost(N, weights):
    MOD = 10**9 + 7
    total_sum = 0
    for i in range(N):
        total_sum += weights[i] * (i + 1) * (N - i) % MOD
    return total_sum % MOD

N = 2
weights = [1, 2]
print(total_cost(N, weights))

N = 4
weights = [1, 1, 1, 1]
print(total_cost(N, weights))

N = 10
weights = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(total_cost(N, weights))