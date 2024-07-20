def compute_values(T, cases):
    mod = 10**9 + 7
    results = []
    
    for case in cases:
        N = case
        total_sum = 0
        for i in range(N+1):
            total_sum += (i**5) % mod
        results.append(total_sum % mod)

    return results

T = 4
cases = [4, 6, 10, 1000000000]
print(*compute_values(T, cases), sep="\n")