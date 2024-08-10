def max_value(N, A):
    for K in range(1, 2**N):
        max_val = 0
        for i in range(K):
            for j in range(i+1, K+1):
                max_val = max(max_val, A[i] + A[j])
        print(max_val)