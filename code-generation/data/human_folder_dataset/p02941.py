import sys
import numpy as np
import numba
from numba import njit, b1, i4, i8, f8

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

@njit((i8[:], i8[:]), cache=True)
def main(A, B):
    N = len(A)
    st, p = np.arange(1 << 20), N
    ans = 0
    while p:
        i, p = st[p - 1], p - 1
        i %= N
        a, b, c = B[i - 1], B[i], B[(i + 1) % N]
        if b < a + c:
            continue
        if b == A[i]:
            continue
        k = (B[i] - A[i]) // (a + c)
        ans += k
        B[i] -= (a + c) * k
        st[p], p = i - 1, p + 1
        st[p], p = i + 1, p + 1
    return ans if np.all(A == B) else -1

N = int(readline())
A = np.array(readline().split(), np.int64)
B = np.array(readline().split(), np.int64)

print(main(A, B))