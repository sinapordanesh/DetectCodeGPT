def patisserie_atcoder(X, Y, Z, K, A, B, C):
    sums = []
    for a in A:
        for b in B:
            for c in C:
                sums.append(a + b + c)
    
    sums.sort(reverse=True)
    
    for i in range(K):
        print(sums[i])