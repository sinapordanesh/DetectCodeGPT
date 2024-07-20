import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def main(A, X, Y):
    N = len(A)
    count = np.zeros(N + 1, np.int64)
    covered = np.zeros(N + 1, np.int64)
    for x in A:
        count[x] += 1
        y = x - count[x] + 1
        if y > 0:
            covered[y] += 1
    spell = np.sum(covered[1:] == 0)
    for i in range(len(X)):
        x, y = X[i], Y[i]
        before = A[x - 1]
        after = y
        A[x - 1] = y
        rem = before - count[before] + 1
        count[before] -= 1
        add = after - count[after]
        count[after] += 1
        if rem > 0:
            covered[rem] -= 1
            if not covered[rem]:
                spell += 1
        if add > 0:
            if not covered[add]:
                spell -= 1
            covered[add] += 1
        print(spell)

if sys.argv[-1] == 'ONLINE_JUDGE':
    import numba
    from numba.pycc import CC
    i8 = numba.from_dtype(np.int64)
    signature = (i8[:], i8[:], i8[:])

    cc = CC('my_module')
    cc.export('main', signature)(main)
    cc.compile()

from my_module import main

N, M = map(int, readline().split())
A = np.array(readline().split(), np.int64)
XY = np.array(read().split(), np.int64)
X = XY[::2]
Y = XY[1::2]

main(A, X, Y)