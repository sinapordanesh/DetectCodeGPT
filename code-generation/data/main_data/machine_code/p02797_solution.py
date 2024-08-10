def find_sequence(N, K, S):
    if K == 0:
        return [S]*N
    else:
        return [1]*K + [S-K+1]*(N-K)