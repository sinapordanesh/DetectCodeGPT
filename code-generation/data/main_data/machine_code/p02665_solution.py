def max_vertices(N, A):
    total_leaves = sum(A)
    current_vertices = 1
    for i in range(N+1):
        if current_vertices < A[i]:
            return -1
        current_vertices = min(2*(current_vertices - A[i]), 2*(current_vertices - A[i]) + A[i])
    return total_leaves

N = 3
A = [0, 1, 1, 2]
print(max_vertices(N, A))

N = 4
A = [0, 0, 1, 0, 2]
print(max_vertices(N, A))

N = 2
A = [0, 3, 1]
print(max_vertices(N, A))

N = 1
A = [1, 1]
print(max_vertices(N, A))

N = 10
A = [0, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(max_vertices(N, A))