import string
import sys

S = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"

mod = 10**9 + 9; p = 13; q = 19
L = 1000
p_table = [1]*(L+1); q_table = [1]*(L+1)
for i in range(L):
    p_table[i+1] = p_table[i] * p % mod
    q_table[i+1] = q_table[i] * q % mod
readline = sys.stdin.readline
write = sys.stdout.write
def to_hash(S, W, H):
    D = [[0]*(W+1) for i in range(H+1)]
    for i in range(H):
        su = 0
        dp = D[i]
        di = D[i+1]
        si = S[i]
        for j in range(W):
            su = (su*p + si[j]) % mod
            di[j+1] = (su + dp[j+1]*q) % mod
    return D
mod = 10**9 + 9; p = 13; q = 19
def get(S, x0, y0, x1, y1):
    P = p_table[x1 - x0]; Q = q_table[y1 - y0]
    return (S[y1][x1] - S[y1][x0] * P - S[y0][x1] * Q + S[y0][x0] * (P * Q) % mod) % mod
def rotate(S, W, H):
    T = [[0]*H for i in range(W)]
    for i in range(H):
        for j in range(W):
            T[j][H-1-i] = S[i][j]
    return T
def mirror(S, W, H):
    T = [[0]*W for i in range(H)]
    for i in range(H):
        for j in range(W):
            T[i][W-1-j] = S[i][j]
    return T


def solve():
    W, H, P = map(int, readline().split())
    if W == H == P == 0:
        return False
    D = S.index
    C = []
    for i in range(H):
        data = readline().strip()
        cs = []
        for c in data:
            v = D(c)
            for k in range(5, -1, -1):
                cs.append(v & (1 << k) > 0)
        C.append(cs)
    E = []
    for i in range(P):
        data = readline().strip()
        es = []
        for c in data:
            v = D(c)
            for k in range(5, -1, -1):
                es.append(v & (1 << k) > 0)
        E.append(es)
    E0 = E
    sv = set()
    for k in range(4):
        sv.add(to_hash(E, P, P)[-1][-1])
        E = rotate(E, P, P)
    E = mirror(E0, P, P)
    for k in range(4):
        sv.add(to_hash(E, P, P)[-1][-1])
        E = rotate(E, P, P)
    F = to_hash(C, W, H)
    ans = 0
    for i in range(H-P+1):
        for j in range(W-P+1):
            if get(F, j, i, j+P, i+P) in sv:
                ans += 1
    write("%d\n" % ans)
    return True
while solve():
    ...
