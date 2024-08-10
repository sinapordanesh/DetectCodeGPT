def max_taste_sum(T, test_cases):
    results = []
    for i in range(T):
        N, D = test_cases[i]
        if N % 2 == 0:
            results.append(D * (N // 2))
        else:
            results.append(127 * (N // 2) + D)
    return results