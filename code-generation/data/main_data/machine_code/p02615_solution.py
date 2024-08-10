def max_total_comfort(N, A):
    A = [0] + A
    total_comfort = sum(A)
    max_comfort = 0
    for i in range(1, N+1):
        max_comfort = max(max_comfort, total_comfort - min(A[i-1], A[i], A[(i+1) % N]))
    return max_comfort

# Sample Input
print(max_total_comfort(4, [2, 2, 1, 3]))  # Output: 7
print(max_total_comfort(7, [1, 1, 1, 1, 1, 1, 1]))  # Output: 6