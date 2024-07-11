import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

"""
列ベクトルが M 個ある
いくつかを選ぶ（和をとる）→すべての行が0となる選び方：0、その他：2^{N-1}通り
列ベクトル空間の生成する次元：d次元
ans = 2^{N-1} * (2^M - 2^[M-d})
= 2^{N+M-1} * (1-2^{-rank})
"""

import numpy as np
MOD = 998244353
N,M = map(int,input().split())
A = np.array([[int(x) for x in input().split()] for _ in range(N)])

def rank(A):
    # F_2 上の行列のrank
    N,M = A.shape
    if N == 0 or M == 0:
        return 0
    nz = np.nonzero(A[0])[0]
    if len(nz) == 0:
        # first col = zero
        return rank(A[1:])
    i = nz[0]
    # swap
    temp = A[:,i].copy()
    A[:,i] = A[:,0]
    A[:,0] = temp
    # (0,0) 成分が 1 になった。行基本変形。
    A ^= A[0][None,:] * A[:,0][:,None]
    return 1 + rank(A[1:,1:])

d = rank(A)
answer = pow(2,N+M-1,MOD) * (1 - pow(2,(-d)%(MOD-1), MOD)) % MOD
print(answer)