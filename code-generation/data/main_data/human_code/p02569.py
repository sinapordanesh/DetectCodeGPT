import sys
import numpy as np
import numba
from numba import njit, b1, i4, i8, f8

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

@njit((numba.types.optional(i8[:]), ) * 2, cache=True)
def seg_f(x, y):
    if x is None:
        return y
    if y is None:
        return x
    a0, a1, ainv = x
    b0, b1, binv = y
    c0, c1, cinv = a0 + b0, a1 + b1, ainv + binv + a1 * b0
    return np.array([c0, c1, cinv], np.int64)


@njit((b1, b1), cache=True)
def lazy_f(a, b):
    return a ^ b


@njit((i8[:], b1), cache=True)
def operate_f(x, a):
    if not a:
        return x
    x0, x1, xinv = x
    x0, x1, xinv = x1, x0, x0 * x1 - xinv
    return np.array([x0, x1, xinv], np.int64)


@njit((i8[:, :], b1[:], i8), cache=True)
def _eval_at(seg, lazy, i):
    return operate_f(seg[i], lazy[i])


@njit((i8[:, :], b1[:], i8), cache=True)
def _propagate_at(seg, lazy, i):
    seg[i] = _eval_at(seg, lazy, i)
    lazy[i << 1] = lazy_f(lazy[i << 1], lazy[i])
    lazy[i << 1 | 1] = lazy_f(lazy[i << 1 | 1], lazy[i])
    lazy[i] = 0


@njit((i8[:, :], ), cache=True)
def build(raw_data):
    N = len(raw_data)
    seg = np.empty((N + N, 3), np.int64)
    seg[N:] = raw_data
    for i in range(N - 1, 0, -1):
        seg[i] = seg_f(seg[i << 1], seg[i << 1 | 1])
    return seg


@njit((i8[:, :], b1[:], i8), cache=True)
def _propagate_above(seg, lazy, i):
    H = 0
    while 1 << H <= i:
        H += 1
    for h in range(H - 1, 0, -1):
        _propagate_at(seg, lazy, i >> h)


@njit((i8[:, :], b1[:], i8), cache=True)
def _recalc_above(seg, lazy, i):
    while i > 1:
        i >>= 1
        seg[i] = seg_f(_eval_at(seg, lazy, i << 1),
                       _eval_at(seg, lazy, i << 1 | 1))


@njit((i8[:, :], b1[:], i8, i8), cache=True)
def set_val(seg, lazy, i, x):
    N = len(seg) // 2
    i += N
    _propagate_above(seg, lazy, i)
    seg[i], lazy[i] = x, 0
    _recalc_above(seg, lazy, i)


@njit((i8[:, :], b1[:], i8, i8), cache=True)
def fold(seg, lazy, l, r):
    N = len(seg) // 2
    l, r = l + N, r + N
    _propagate_above(seg, lazy, l // (l & -l))
    _propagate_above(seg, lazy, r // (r & -r) - 1)
    vl = vr = None
    while l < r:
        if l & 1:
            vl = seg_f(vl, _eval_at(seg, lazy, l))
            l += 1
        if r & 1:
            r -= 1
            vr = seg_f(_eval_at(seg, lazy, r), vr)
        l, r = l >> 1, r >> 1
    return seg_f(vl, vr)


@njit((i8[:, :], b1[:], i8, i8, i8), cache=True)
def operate_range(seg, lazy, l, r, x):
    N = len(seg) // 2
    l, r = l + N, r + N
    l0, r0 = l // (l & -l), r // (r & -r) - 1
    _propagate_above(seg, lazy, l0)
    _propagate_above(seg, lazy, r0)
    while l < r:
        if l & 1:
            lazy[l] = lazy_f(lazy[l], x)
            l += 1
        if r & 1:
            r -= 1
            lazy[r] = lazy_f(lazy[r], x)
        l, r = l >> 1, r >> 1
    _recalc_above(seg, lazy, l0)
    _recalc_above(seg, lazy, r0)

@njit((i8, i8[:], i8[:]), cache=True)
def main(N, A, TLR):
    seg_raw = np.empty((N, 3), np.int64)
    for i in range(N):
        if A[i] == 0:
            seg_raw[i] = (1, 0, 0)
        elif A[i] == 1:
            seg_raw[i] = (0, 1, 0)
    seg = build(seg_raw)
    lazy = np.zeros(len(seg), np.bool_)
    for i in range(0, len(TLR), 3):
        t, l, r = TLR[i:i + 3]
        l -= 1
        if t == 1:
            operate_range(seg, lazy, l, r, 1)
        else:
            print(fold(seg, lazy, l, r)[2])

N, Q = map(int, readline().split())
A = np.array(readline().split(), np.int64)
TLR = np.array(read().split(), np.int64)

main(N, A, TLR)