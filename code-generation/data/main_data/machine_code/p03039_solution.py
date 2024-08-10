def sum_of_costs(N, M, K):
    MOD = 10**9 + 7
    result = 0
    for x in range(1, N + 1):
        for y in range(1, M + 1):
            for i in range(1, N + 1):
                for j in range(1, M + 1):
                    cost = abs(x - i) + abs(y - j)
                    result += cost
    return result % MOD

# Test the function
print(sum_of_costs(2, 2, 2))
print(sum_of_costs(4, 5, 4))
print(sum_of_costs(100, 100, 5000))