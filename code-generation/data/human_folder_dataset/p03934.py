import sys
import numpy as np
import numba
from numba import njit
i8 = numba.int64

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

@njit((i8[:], ), cache=True)
def build(raw_data):
    bit = raw_data.copy()
    for i in range(len(bit)):
        j = i + (i & (-i))
        if j < len(bit):
            bit[j] += bit[i]
    return bit


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


@njit((i8[:], i8), cache=True)
def find_kth_element(bit, k):
    N = len(bit)
    x, sx = 0, 0
    dx = 1
    while 2 * dx < N:
        dx *= 2
    while dx:
        y = x + dx
        if y < N:
            sy = sx + bit[y]
            if sy < k:
                x, sx = y, sy
        dx //= 2
    return x + 1

@njit((i8, i8[:]), cache=True)
def main(N, AB):
    A, B = AB[::2], AB[1::2]
    Q = len(A)

    bit = np.zeros(N + 1, np.int64)  # 長方形の右上になる x 座標集合を管理
    bit_raw = np.zeros(N + 1, np.int64)
    H = np.zeros(N + 1, np.int64)  # 長方形の高さを管理
    H[0] = 2 * 10**13 + 10
    bit_raw[N] = 1
    add(bit, N, 1)

    for i in range(Q):
        a, b = A[i], B[i]
        n = get_sum(bit, a - 1)
        h = H[find_kth_element(bit, 1 + n)]
        if not bit_raw[a]:
            bit_raw[a] = 1
            add(bit, a, 1)
            H[a] = h
        r = a

        while b:
            l = 0 if n == 0 else find_kth_element(bit, n)
            n -= 1
            area = (H[l] - H[r]) * (r - l)
            if area <= b:
                b -= area
                if l:
                    bit_raw[l] = 0
                    add(bit, l, -1)
                H[l], H[r] = 0, H[l]
                continue
            k = b // (r - l)
            b -= k * (r - l)
            H[r] += k
            if b:
                m = l + b
                bit_raw[m] = 1
                add(bit, m, 1)
                H[m] = H[r] + 1
                b = 0
    for n in range(N, 0, -1):
        H[n - 1] = max(H[n - 1], H[n])
    return H[1:N + 1]

N, Q = map(int, readline().split())
AB = np.array(read().split(), np.int64)

ans = main(N, AB)
print('\n'.join(map(str, ans.tolist())))