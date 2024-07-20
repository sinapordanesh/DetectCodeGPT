def sum_operations(A, B, C, K):
    for _ in range(K):
        A, B, C = B+C, A+C, A+B
        if abs(A-B) > 10**18:
            return "Unfair"
    return A - B