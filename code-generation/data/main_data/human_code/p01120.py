import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve(C, N, M, range = range, min = min):
    K = N // 4 + 1
    S = [0]*K
    T = [0]*K
    U = [0]*(K+1)
    for i in range(N-1):
        U[0] = 10**18
        for j in range(K):
            U[j+1] = min(U[j], S[j])
        k = K-1
        ci = C[i]; cj = C[i+1]
        r = 10**18
        for j in range(K-1, -1, -1):
            while ci + k*M > cj + j*M:
                r = min(r, ci + k*M + S[k])
                k -= 1
            T[j] = min(r - j*M - cj, U[k+1])
        S, T = T, S
    ci = C[-1]
    for i in range(K):
        S[i] += ci + i*M
    write("%d\n" % min(S))
while 1:
    N, M = map(int, readline().split())
    if N == 0:
        break
    *A, = map(int, readline().split())
    *B, = map(int, readline().split())
    C = [(b - a) % M for a, b in zip(A, B)]
    solve(C, N, M)
