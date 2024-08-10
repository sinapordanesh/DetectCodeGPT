import sys
import numpy as np
import heapq as hp

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def compute(A, B, X):
    """左からn番の人まで。AからX人とる。ときの最大スコアを返す。"""
    result = np.zeros(len(A), np.int64)
    result[X - 1] = A[:X].sum()
    q = []
    for i in range(X):
        q.append(A[i] - B[i])
    hp.heapify(q)
    for i in range(X, len(A)):
        x = result[i - 1] + A[i]  # とりあえず A をとる
        loss = hp.heappushpop(q, A[i] - B[i])  # ひとつ B に取り換えたときのロス
        result[i] = x - loss
    return result

if sys.argv[-1] == 'ONLINE_JUDGE':
    import numba
    from numba.pycc import CC
    i8 = numba.from_dtype(np.int64)
    sig = (i8[:], i8[:], i8)

    cc = CC('my_module')
    cc.export('compute', sig)(compute)
    cc.compile()

from my_module import compute

def main(ABC, X, Y, Z):
    A = ABC[::3]
    B = ABC[1::3]
    C = ABC[2::3]
    ind = np.argsort(C - A)
    A, B, C = A[ind], B[ind], C[ind]
    dp1 = compute(A, B, X)
    dp2 = compute(C[::-1], B[::-1], Z)[::-1]
    x = dp1[X - 1:X + Y] + dp2[X:X + Y + 1]
    return x.max()

X, Y, Z = map(int, readline().split())
ABC = np.array(read().split(), np.int64)

print(main(ABC, X, Y, Z))