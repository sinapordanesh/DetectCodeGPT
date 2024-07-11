from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    N, M = map(int, readline().split())
    if N == M == 0:
        return False
    ca = ord('a')
    E = [list(map(lambda x: ord(x)-ca, readline().strip())) for i in range(N)]
    F = "".join(readline().strip() for i in range(M))
    L = sum(map(len, E))
    MOD = 10**9 + 9; base = 37
    ALL = (1 << N) - 1; bALL = (1 << (1 << N)) - 1
    pw = [1]*(L+1)
    for i in range(L):
        pw[i+1] = pw[i] * base % MOD
    V = [0]*N; P = [0]*N; K = [0]*N
    S = [0]*N
    for i in range(N):
        v = 0
        for c in E[i]:
            v = (v * base + c) % MOD
        V[i] = v
        K[i] = len(E[i])
        P[i] = pw[K[i]]
        r = bALL
        for s in range(ALL + 1):
            if s & (1 << i):
                r ^= 1 << s
        S[i] = r

    A = len(F)
    dp = [1] * (A+1)
    H = [0]*(A+1)
    ans = s = 0
    for i in range(A):
        H[i+1] = s = (s * base + (ord(F[i]) - ca)) % MOD
        r = 1
        for j in range(N):
            if K[j] <= i+1 and (s - H[i+1 - K[j]] * P[j]) % MOD == V[j]:
                r |= (dp[i+1 - K[j]] & S[j]) << (1 << j)
        dp[i+1] = r
        if r & (1 << ALL):
            ans += 1
    write("%d\n" % ans)
    return True
while solve():
    ...
