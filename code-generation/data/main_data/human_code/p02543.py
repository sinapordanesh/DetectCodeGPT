import sys
import numpy as np
import numba
from numba import njit, b1, i4, i8, f8

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

K = 20

@njit((i8[:],i8), cache=True)
def build_sp(X, D):
    INF = 1<<60
    N = len(X)
    X = np.append(X, INF)
    sp = np.empty((K,N+1), np.int64)
    sp_sum = np.empty((K,N+1), np.int64)
    sp[0] = np.searchsorted(X, X + D)
    sp[0,-1] = N
    sp_sum[0] = sp[0] # 移動先の座標の和
    for k in range(1, K):
        for n in range(N+1):
            to = sp[k-1,n]
            sp[k][n] = sp[k-1][to]
            sp_sum[k][n] = sp_sum[k-1,n] + sp_sum[k-1,to]
    return sp, sp_sum

@njit((i8[:,:],i8[:,:],i8,i8), cache=True)
def largest_set(sp, sp_sum, l, r):
    # 要素数と座標の和
    ret = [1,l]
    for k in range(K-1, -1, -1):
        # 2^k 進めるなら進む
        if sp[k,l] <= r:
            ret[0] += 1<<k
            ret[1] += sp_sum[k,l]
            l = sp[k,l]
    return ret

@njit((i8[:],i8,i8[:]), cache=True)
def main(X, D, LR):
    N = len(X)
    spl, spl_sum = build_sp(X, D)
    spr, spr_sum = build_sp(-X[::-1], D)
    for i in range(0, len(LR), 2):
        l, r = LR[i:i+2]
        l, r = l-1, r-1
        cl, sl = largest_set(spl, spl_sum, l,r)
        cr, sr = largest_set(spr, spr_sum, N-1-r, N-1-l)
        sr = (N-1)*cr-sr
        print(cl + sr - sl)

N, D = map(int, readline().split())
X = np.array(readline().split(), np.int64)
Q = int(readline())
LR = np.array(read().split(), np.int64)

main(X,D,LR)