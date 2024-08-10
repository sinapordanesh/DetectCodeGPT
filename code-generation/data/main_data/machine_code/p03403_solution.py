def canceled_trip_cost(N, A):
    total_cost = sum([abs(A[i] - A[i-1]) for i in range(1, N)])
    
    result = []
    for i in range(N):
        if i == 0:
            result.append(total_cost - abs(A[0] - A[1]))
        elif i == N-1:
            result.append(total_cost - abs(A[N-2] - A[N-1]))
        else:
            result.append(total_cost - abs(A[i-1] - A[i]) - abs(A[i] - A[i+1]) + abs(A[i-1] - A[i+1]))
    
    return result

# Sample Input 1
N = 3
A = [3, 5, -1]
print(*canceled_trip_cost(N, A))

# Sample Input 2
N = 5
A = [1, 1, 1, 2, 0]
print(*canceled_trip_cost(N, A))

# Sample Input 3
N = 6
A = [-679, -2409, -3258, 3095, -3291, -4462]
print(*canceled_trip_cost(N, A))