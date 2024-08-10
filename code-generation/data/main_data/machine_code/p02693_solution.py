def practice_golf(K, A, B):
    for i in range(A, B+1):
        if i % K == 0:
            return "OK"
    return "NG"