import sys
import numpy as np
import numba
from numba import njit, b1, i4, i8, f8

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

@njit((i8[:], i8), cache=True)
def get_sum(bit, i):
    s = 0
    while i:
        s += bit[i]
        i -= i & -i
    return s


@njit((i8[:], i8, i8), cache=True)
def add(bit, i, x):
    while i < len(bit):
        bit[i] += x
        i += i & -i

@njit((i8, i8[:]), cache=True)
def main(M, LR):
    L, R = LR[::2], LR[1::2]
    R = R + 1
    D = R - L
    argsort = np.argsort(D)
    L, R, D = L[argsort], R[argsort], D[argsort]
    idx = np.searchsorted(D, np.arange(M + 2))

    bit = np.zeros(M + 10, np.int64)
    rest = len(L)
    for d in range(1, M + 1):
        # 長さ d の区間を追加
        for i in range(idx[d], idx[d + 1]):
            rest -= 1
            add(bit, L[i], 1)
            add(bit, R[i], -1)
        ans = rest
        for n in range(d, M + 1, d):
            ans += get_sum(bit, n)
        print(ans)

N, M = map(int, readline().split())
LR = np.array(read().split(), np.int64)

main(M, LR)