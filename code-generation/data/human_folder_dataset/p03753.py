import sys
import numpy as np
import numba
from numba import njit, b1, i4, i8

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

@njit((i8, i8, i8[:]), cache=True)
def solve_naive(H, M, A):
    visited = np.zeros(7 * H, np.bool_)
    for a in A:
        visited[a::M] = 1
    st = np.empty(7 * H + 10, np.int64)
    ncomp = 0
    for v in range(7 * H):
        if visited[v]:
            continue
        ncomp += 1
        st[0] = v
        p = 1
        while p:
            p -= 1
            v = st[p]
            x, y = divmod(v, 7)
            for d in (1, -1, 7, -7):
                w = v + d
                if w < 0 or w >= 7 * H:
                    continue
                x1, y1 = divmod(w, 7)
                if abs(x - x1) + abs(y - y1) != 1:
                    continue
                if visited[w]:
                    continue
                visited[w] = True
                st[p] = w
                p += 1
    return ncomp

N, M, Q = map(int, readline().split())
A = np.array(readline().split(), np.int64)

if N <= 5 * M:
    x = solve_naive(N, M, A)
else:
    q, r = divmod(N, M)
    a, b = solve_naive(r + 3 * M, M, A), solve_naive(r + 4 * M, M, A)
    x = a + (q - 3) * (b - a)
print(x)