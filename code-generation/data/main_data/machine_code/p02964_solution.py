def elements_of_s(N, K, A):
    s = []
    X = []
    for i in range(N):
        X += A
    
    for i in range(N*K):
        if X[i] not in s:
            s.append(X[i])
        else:
            while s[-1] != X[i]:
                s.pop()
    
    return s