import sys
import numpy as np
import numba
from numba import njit, b1, i4, i8, f8

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 998_244_353

@njit((i8, i8[:, :]), cache=True)
def precompute(N, G):
    ng = np.zeros(N + 10, np.bool_)
    g = np.zeros(N + 1, np.int64)
    ind = np.searchsorted(G[:, 0], np.arange(N + 10))
    for v in range(N - 1, 0, -1):
        for i in range(ind[v], ind[v + 1]):
            w = G[i, 1]
            ng[g[w]] = 1
        for n in range(N + 10):
            if ng[n]:
                continue
            break
        g[v] = n
        for i in range(ind[v], ind[v + 1]):
            w = G[i, 1]
            ng[g[w]] = 0

    B = 10**18 % MOD
    power = 1
    A = np.zeros(1024, np.int64)
    for i in range(1, N + 1):
        power = power * B % MOD
        A[g[i]] += power
    return A % MOD

@njit((i8[:], i8[:]), cache=True)
def convolve(A, B):
    C = np.zeros(1024, np.int64)
    for i in range(1024):
        for j in range(1024):
            C[i ^ j] += A[i] * B[j] % MOD
    return C % MOD

N = int(readline())
nums = np.array(read().split(), np.int64)
graphs = []
for _ in range(3):
    M = nums[0]
    G = nums[1:1 + 2 * M].reshape(M, 2)
    G.sort(axis=1)
    G = G[np.argsort(G[:, 0])]
    graphs.append(G)
    nums = nums[1 + 2 * M:]

G1, G2, G3 = map(lambda G: precompute(N, G), graphs)

print(convolve(convolve(G1, G2), G3)[0])