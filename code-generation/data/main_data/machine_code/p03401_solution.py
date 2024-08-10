def canceled_spot_cost(N, A):
    total_cost = sum(abs(A[i] - A[i-1]) for i in range(1, N))
    result = [total_cost] * N
    for i in range(N):
        if i == 0:
            result[i] -= abs(A[i])
        elif i == N-1:
            result[i] -= abs(A[N-2])
        else:
            result[i] -= abs(A[i] - A[i-1]) + abs(A[i] - A[i+1])
    return result