def min_operations(N, K, A):
    operations = 0
    while any(A[i:i+K] != [min(A[i:i+K])]*K for i in range(N-K+1)):
        min_val = min(A)
        idx = A.index(min_val)
        for i in range(idx, min(N, idx+K)):
            A[i] = min_val
        operations += 1
    return operations

# Sample Input 1
print(min_operations(4, 3, [2, 3, 1, 4]))

# Sample Input 2
print(min_operations(3, 3, [1, 2, 3]))

# Sample Input 3
print(min_operations(8, 3, [7, 3, 1, 8, 4, 6, 2, 5]))