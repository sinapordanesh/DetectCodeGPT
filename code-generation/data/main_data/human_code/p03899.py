import sys
import numpy as np
import numba
from numba import njit, b1, i4, i8
from numba.types import Omitted

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

@njit((i8[:], i8, i8), cache=True)
def main(A, M, K):
    # 右端ごとの最高得点を管理。まずは 1 回目。
    INF = 1 << 60
    dp = A.copy()

    q = np.empty(len(A) + 100, np.int32)
    q[:2] = 2, 2

    def push(q, x):
        q[q[1]] = x
        q[1] += 1

    def is_empty(q):
        return q[0] == q[1]

    for k in range(2, K + 1):
        newdp = np.full_like(A, -INF)
        q[:2] = 2, 2
        for i in range(len(A)):
            if not is_empty(q):
                x = dp[q[q[0]]]
                newdp[i] = x + A[i] * k
            x = dp[i]
            while not is_empty(q) and dp[q[q[1] - 1]] < x:
                q[1] -= 1
            push(q, i)
            while q[q[0]] <= i - M:
                q[0] += 1
        dp = newdp
    return dp.max()

N, M, K = map(int, readline().split())
A = np.array(read().split(), np.int64)

print(main(A, M, K))