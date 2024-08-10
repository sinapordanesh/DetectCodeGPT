def min_abs_diff(N, A):
    A.sort()
    return min(A[N-1] - A[0], A[N-2] - A[1], A[N-3] - A[2])

# Sample Input 1
print(min_abs_diff(5, [3, 2, 4, 1, 2]))

# Sample Input 2
print(min_abs_diff(10, [10, 71, 84, 33, 6, 47, 23, 25, 52, 64]))

# Sample Input 3
print(min_abs_diff(7, [1, 2, 3, 1000000000, 4, 5, 6]))