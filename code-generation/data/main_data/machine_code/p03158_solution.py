def find_sum_of_integers(N, Q, A, X):
    result = []
    for i in range(Q):
        x = X[i]
        sum_takahashi = 0
        index = N - 1
        for j in range(N):
            if A[j] <= x:
                index = j
            else:
                sum_takahashi += A[j]
        
        if index == N - 1:
            sum_takahashi += A[N - 1]
        else:
            if abs(A[index] - x) <= abs(A[index + 1] - x):
                sum_takahashi += A[index]
            else:
                sum_takahashi += A[index + 1]
        
        result.append(sum_takahashi)
    
    return result

# Sample Input
N = 5
Q = 5
A = [3, 5, 7, 11, 13]
X = [1, 4, 9, 10, 13]

print(*find_sum_of_integers(N, Q, A, X))

N = 4
Q = 3
A = [10, 20, 30, 40]
X = [2, 34, 34]

print(*find_sum_of_integers(N, Q, A, X))