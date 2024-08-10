import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 10**9 + 7

def precompute(M):
    # 残り M 秒あるとする。
    # dp1：人数
    # dp2：生産開始時刻の総和
    g = M + 10
    dp1 = np.ones(M, np.int64)
    dp2 = np.zeros(M, np.int64)
    while g * (g - 1) // 2 > M:
        g -= 1
    while g >= 1:
        newdp1 = np.ones_like(dp1)
        newdp2 = np.zeros_like(dp2)
        for m in range(2 * g, M):
            newdp1[m] = (newdp1[m - g] + dp1[m - g]) % MOD
            newdp2[m] = (newdp2[m - g] + dp2[m - g] + g * newdp1[m]) % MOD
        g -= 1
        dp1, dp2 = newdp1, newdp2
    return dp1, dp2

def main(NC):
    dp1, dp2 = precompute(100_010)
    N, C = NC[::2], NC[1::2]
    for i in range(len(N)):
        n, c = N[i], C[i]
        q, r = divmod(n, c)
        ans = dp1[q] * n - dp2[q] * c
        print(ans % MOD)

if sys.argv[-1] == 'ONLINE_JUDGE':
    import numba
    from numba.pycc import CC
    i8 = numba.int64
    cc = CC('my_module')

    def cc_export(f, signature):
        cc.export(f.__name__, signature)(f)
        return numba.njit(f)

    precompute = cc_export(precompute, (i8, ))
    main = cc_export(main, (i8[:], ))
    cc.compile()

from my_module import main

NC = np.array(read().split(), np.int64)[1:]

main(NC)