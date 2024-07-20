def min_operations_required(N, A):
    X = [0] * N
    count = 0
    for i in range(N-1):
        if A[i] > X[i]:
            diff = A[i] - X[i]
            X[i] = A[i]
            X[i+1] += diff
            count += diff
        elif A[i] < X[i]:
            return -1
    if A[-1] != X[-1]:
        return -1
    return count

#Sample Input 1
print(min_operations_required(4, [0, 1, 1, 2]))

#Sample Input 2
print(min_operations_required(3, [1, 2, 1]))

#Sample Input 3
print(min_operations_required(9, [0, 1, 1, 0, 1, 2, 2, 1, 2]))