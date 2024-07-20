def possible_values(N, X, D):
    if D == 0:
        if X == 0:
            return 1
        else:
            return N + 1
    
    X = abs(X)
    mod = X % abs(D)
    
    if mod == 0:
        start = X // abs(D)
    else:
        start = X // abs(D)
    
    max_possible = N * (N - 1) // 2
    
    if start >= N:
        return max_possible
    
    diff = max_possible - start * (N - start)
    return diff + 1 + (start + 1) * start // 2 + (N - start + 1) * (N - start) // 2

N, X, D = map(int, input().split())
print(possible_values(N, X, D))