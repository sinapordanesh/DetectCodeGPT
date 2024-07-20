def mul(A, B, N, M):
    result = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            tmp = 0
            for k in range(N):
                tmp += A[i][k] * B[k][j]
                tmp %= M
            result[i][j] = tmp
    return result

while 1:
    N, M, A, B, C, T = map(int, input().split())
    if N == 0:
        break
    *S, = map(int, input().split())
    P = [[0]*N for i in range(N)]
    for i in range(N):
        P[i][i] = B
    for i in range(N-1):
        P[i+1][i] = A
        P[i][i+1] = C
    base = [[0]*N for i in range(N)]
    for i in range(N):
        base[i][i] = 1
    while T:
        if T & 1:
            base = mul(base, P, N, M)
        P = mul(P, P, N, M)
        T >>= 1
    U = [0]*N
    for i in range(N):
        tmp = 0
        for j in range(N):
            tmp += base[i][j] * S[j]
            tmp %= M
        U[i] = tmp
    print(*U)