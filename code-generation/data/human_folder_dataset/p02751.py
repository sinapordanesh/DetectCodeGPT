import sys
sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))
import numpy as np
def resolve():
    N, M = lr()
    rev = 0
    if N < M:
        M, N = N, M
        rev = 1
    T = np.zeros(1, dtype=np.int8)
    for i in range(N):
        T = np.tile(T, (2, 2))
        T[1<<i:, 1<<i:] ^= 1
    T = np.diff(T, axis=0)
    T = np.diff(T, axis=1)
    T = T[:, :(1<<M)-1]%2
    if rev:
        T = np.transpose(T)
    for t in T:
        print(''.join(t.astype(str)))
resolve()