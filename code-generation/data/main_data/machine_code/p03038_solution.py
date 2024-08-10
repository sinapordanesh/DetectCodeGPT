def max_sum(N, M, A, operations):
    for b, c in operations:
        sorted_A = sorted(A, reverse=True)
        for i in range(b):
            if i >= len(sorted_A):
                break
            if sorted_A[i] < c:
                sorted_A[i] = c
        A = sorted_A
    return sum(A)