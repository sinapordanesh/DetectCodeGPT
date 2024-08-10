from collections import defaultdict
import sys
readline = sys.stdin.readline
write = sys.stdout.write

MOD = 10**9 + 9

def matmul(N, A, B):
    C = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(N)) % MOD
    return C

def prepare(N, H):
    mat = [[0]*N for i in range(N)]
    res = []
    for i in range(N):
        mat[i][i] = 1
    res.append([e[:] for e in mat])
    for i in range(N-1):
        mat[i][i+1] = mat[i+1][i] = 1
    res.append([e[:] for e in mat])
    while H:
        mat = matmul(N, mat, mat)
        res.append([e[:] for e in mat])
        H >>= 1
    return res
def matpow(X, N, h, MS):
    k = 1
    while h:
        if h & 1:
            mat = MS[k]
            X = [sum(ai*xi for ai, xi in zip(mat_i, X)) % MOD for mat_i in mat]
        h >>= 1
        k += 1
    return X

cnt = 1
def solve():
    W, H, N = map(int, readline().split())
    if W == H == N == 0:
        return False
    P = defaultdict(list)
    for i in range(N):
        x, y = map(int, readline().split())
        if y > 1:
            P[y-1].append(x-1)
    MS = prepare(W, H)
    *S, = P.items()
    S.sort()
    X = [0]*W
    X[0] = 1
    prv = 0
    for y, vs in S:
        X = matpow(X, W, y-prv, MS)
        for v in vs:
            X[v] = 0
        prv = y
    if prv < H-1:
        X = matpow(X, W, H-1-prv, MS)
    write("Case %d: %d\n" % (cnt, X[W-1]))
    return True
while solve():
    cnt += 1
