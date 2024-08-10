import sys
import numpy as np
from heapq import heappop, heappush

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def choose_increasing(q):
    A = []
    for x in q:
        while A and A[-1] >= x:
            A.pop()
        A.append(x)
    return np.array(A, np.int64)

def main(A, N):
    heap = [(-A[-1], 1)]
    for n in A[::-1]:
        while True:
            if -heap[0][0] <= n:
                break
            x, coef = heappop(heap)
            while heap and heap[0][0] == x:
                _, c = heappop(heap)
                coef += c
            q, r = divmod(-x, n)
            heappush(heap, (-n, coef * q))
            heappush(heap, (-r, coef))
    ret = np.zeros(N + 10, np.int64)
    for x, c in heap:
        x = -x
        ret[1] += c
        ret[x + 1] -= c
    ret = np.cumsum(ret)
    return ret[1:N + 1]

if sys.argv[-1] == 'ONLINE_JUDGE':
    import numba
    from numba.pycc import CC
    i8 = numba.int64
    cc = CC('my_module')

    def cc_export(f, signature):
        cc.export(f.__name__, signature)(f)
        return numba.njit(f)

    main = cc_export(main, (i8[:], i8))
    cc.compile()

from my_module import main

N, Q = map(int, readline().split())
q = [N] + list(map(int, read().split()))

A = choose_increasing(q)
ans = main(A, N)
print('\n'.join(map(str, ans.tolist())))