def min_total_cost(N, D, A):
    total_cost = 0
    for i in range(1, N):
        total_cost += min(abs(A[i-1] - A[i]) * D + A[i-1] + A[i], D)
    return total_cost
N, D, *A = map(int, input().split())
print(min_total_cost(N, D, A))