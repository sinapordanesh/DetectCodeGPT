import sys
readline = sys.stdin.readline
from math import log2
from itertools import accumulate
N, M = map(int, readline().split())
A = [list(map(int, readline().split())) for i in range(N)]
B = max(max(Ai) for Ai in A)
if M == 1:
    if N == 1 or all(A[i][0] < A[i+1][0] for i in range(N-1)):
        print("0")
    else:
        print("-1")
    exit(0)
logB = log2(B)
logBi = int(logB)
INF = 10**18
INFL = [INF]*(M - logBi-2)
def gen(P, t, L = min(logBi+2, M)):
    if t <= logB:
        # O(M log B)
        for k in range(t):
            P[:] = accumulate(P)
    else:
        # O(log^2 B)
        V = [1]*L # V[k] = C(i-j+t-1, i-j)
        for k in range(1, L):
            V[k] = V[k-1] * (t + k - 1)//k

        for i in range(L-1, 0, -1):
            P[i] += sum(P[j] * V[i-j] for j in range(i))
        if logBi+2 < M:
            P[logBi+2:] = INFL
T = [0]*N
ans = 0
P = [0]*M
for i in range(N-1):
    a0, a1 = A[i][:2]
    b0, b1 = A[i+1][:2]
    if a0 < b0:
        continue
    if a0 > b0:
        ans = -1
        break
    # a1 + a0*t0 = b1 + b0*t1 となる正の整数 t1 が存在するか
    t0 = T[i]
    v = max(t0*a0 + a1 - b1, 0)
    if v % b0 > 0:
        T[i+1] = t1 = (v + b0-1) // b0
        ans += t1
        continue

    # そのような t1 が存在するならばチェック

    t1 = v // b0
    if t0 <= t1:
        # A_i < f(A_{i+1}, t1-t0) となるか
        P[:] = A[i+1]
        gen(P, t1 - t0)
        if P <= A[i]:
            t1 += 1
    else:
        # f(A_i, t0-t1) < A_{i+1} となるか
        P[:] = A[i]
        gen(P, t0 - t1)
        if A[i+1] <= P:
            t1 += 1
    T[i+1] = t1
    ans += t1
print(ans)