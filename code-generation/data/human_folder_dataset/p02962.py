def numba_compile(numba_config):
    import os, sys
    if sys.argv[-1] == "ONLINE_JUDGE":
        from numba import njit
        from numba.pycc import CC
        cc = CC("my_module")
        for func, signature in numba_config:
            globals()[func.__name__] = njit(signature)(func)
            cc.export(func.__name__, signature)(func)
        cc.compile()
        exit()
    elif os.name == "posix":
        exec(f"from my_module import {','.join(func.__name__ for func, _ in numba_config)}")
        for func, _ in numba_config:
            globals()[func.__name__] = vars()[func.__name__]
    else:
        from numba import njit
        for func, signature in numba_config:
            globals()[func.__name__] = njit(signature, cache=True)(func)
        print("compiled!", file=sys.stderr)


import sys
import numpy as np

def z_algo(S):  # [z_algo, "i8[:](i8[:])"],
    # Z-algoirhm  O(n)
    # Z[i] := S と S[i:] で prefix が何文字一致しているか
    # 検証1: https://atcoder.jp/contests/abc150/submissions/15829530
    # 検証2: https://atcoder.jp/contests/abc141/submissions/15855247
    i, j, n = 1, 0, len(S)
    Z = np.zeros(S.shape, dtype=np.int64)
    Z[0] = n
    while i < n:
        while i+j < n and S[j] == S[i+j]:
            j += 1
        if j == 0:
            i += 1
            continue
        Z[i] = j
        d = 1
        while i+d < n and d+Z[d] < j:
            Z[i+d] = Z[d]
            d += 1
        i += d
        j -= d
    return Z

def solve(s, t):
    ns = len(s)
    nt = len(t)
    n = max(ns, nt) * 2
    ts = np.empty(n*4, dtype=np.int64)
    ts[:n*2] = t[np.arange(2*n, dtype=np.int64) % nt]
    ts[n*2:] = s[np.arange(2*n, dtype=np.int64) % ns]
    Z = z_algo(ts)
    ma = Z[n*2:].max()
    if ma > n:
        return -1
    else:
        return ma // nt

numba_compile([
    [z_algo, "i8[:](i8[:])"],
    [solve, "i8(i1[:],i1[:])"],
])

def main():
    s = np.frombuffer(sys.stdin.buffer.readline()[:-1], dtype=np.int8).copy()
    t = np.frombuffer(sys.stdin.buffer.readline()[:-1], dtype=np.int8).copy()
    ans = solve(s, t)
    print(ans)

main()
