def min_distance(K, N, A):
    distances = []
    for i in range(N):
        if i == N-1:
            distances.append(K - (A[i] - A[0]))
        else:
            distances.append(A[i+1] - A[i])
    return K - max(distances)