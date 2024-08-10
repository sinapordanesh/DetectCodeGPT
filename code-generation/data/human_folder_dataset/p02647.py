import sys
import numpy as np
from numba import njit

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


@njit('i8[:](i8,i8,i8[:])', cache=True)
def func(n, k, A):
    for _ in range(k):
        B = np.zeros(n + 1, np.int64)
        for i, a in enumerate(A):
            B[max(0, i - a)] += 1
            B[min(i + a + 1, n)] -= 1
        A = B.cumsum()[:-1]
        if np.all(A == n):
            break
    return A


def main():
    N, K = map(int, readline().split())
    A = np.array(readline().split(), np.int64)
    ans = func(N, K, A)
    print(*ans)


if __name__ == '__main__':
    main()
