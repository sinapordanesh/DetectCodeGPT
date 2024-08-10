import os
import sys
import numpy as np

# >>> binary indexed tree >>>
# 必要な要素数+1 の長さの ndarray の 1 要素目以降を使う

def bit_sum(bit, i):  # [bit_sum, "i8(i8[:],i8)"],
    # (0, i]
    res = 0
    while i:
        res += bit[i]
        i -= i & -i
    return res

def bit_add(bit, i, val):  # [bit_add, "void(i8[:],i8,i8)"],
    n = len(bit)
    while i < n:
        bit[i] += val
        i += i & -i

# <<< binary indexed tree <<<


def inversion_number(arr):  # [inversion_number, "i8(f8[:])"],
    # 転倒数
    n = len(arr)
    arr = np.argsort(arr) + 1
    bit = np.zeros(n+1, dtype=np.int64)
    res = n * (n-1) >> 1
    for val in arr:
        res -= bit_sum(bit, val)
        bit_add(bit, val, 1)
    return res


# >>> numba compile >>

numba_config = [
    [bit_sum, "i8(i8[:],i8)"],
    [bit_add, "void(i8[:],i8,i8)"],
    [inversion_number, "i8(f8[:])"],
]
if sys.argv[-1] == "ONLINE_JUDGE":
    from numba import njit
    from numba.pycc import CC
    cc = CC("my_module")
    for func, signature in numba_config:
        vars()[func.__name__] = njit(signature)(func)
        cc.export(func.__name__, signature)(func)
    cc.compile()
    exit()
elif os.name == "posix":
    exec(f"from my_module import {','.join(func.__name__ for func, _ in numba_config)}")
else:
    from numba import njit
    for func, signature in numba_config:
        vars()[func.__name__] = njit(signature, cache=True)(func)
    print("compiled", file=sys.stderr)

# <<< numba compile <<<


N = int(input())
ABC = [list(map(int, input().split())) for _ in range(N)]
A, B, C = zip(*ABC)
th = N*(N-1)//2 // 2 + 1
def solve(A, B, C):
    # y = (-Ax+C) / B
    if N < 100:
        ok = -1e10
        ng = 1e10
        n_iteration = 70
    else:
        ok = -1e4
        ng = 1e4
        n_iteration = 46
    A, B, C = zip(*sorted(zip(A, B, C), key=lambda x: -x[0]/x[1]))
    A = np.array(A)
    B = np.array(B)
    C = np.array(C)
    for _ in range(n_iteration):
        x = (ok+ng) * 0.5
        Y = (-A*x+C) / B
        inv_num = inversion_number(Y)
        if inv_num >= th:
            ok = x
        else:
            ng = x
    return ok

print(solve(A, B, C), solve(B, A, C))