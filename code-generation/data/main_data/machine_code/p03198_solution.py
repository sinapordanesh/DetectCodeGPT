def min_operations(N, A):
    count = 0
    for i in range(N):
        while A[i+1] < A[i]:
            A[i] *= -2
            count += 1
    return count if sorted(A) == A else -1