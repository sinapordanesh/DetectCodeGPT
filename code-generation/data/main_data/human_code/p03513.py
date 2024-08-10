import sys
import numpy as np
import numba
from numba import njit, b1, i4, i8
from numba.types import Omitted

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 1_000_000_007

@njit((i8, i8[:, :]), cache=True)
def main(N, G):
    pow2 = np.empty(1000, np.int64)
    pow2[0] = 1
    for n in range(1, 1000):
        pow2[n] = pow2[n - 1] * 2 % MOD
    # 部分集合 s に対して、s の中に含まれる辺の個数
    dp1 = np.zeros(1 << N, np.int64)
    for b in range(N):
        for a in range(b):
            if G[a, b]:
                s = 1 << a | 1 << b
                dp1[s] += 1
    for n in range(N):
        for s in range(1 << N):
            t = s | 1 << n
            if s == t:
                continue
            dp1[t] += dp1[s]
    # 部分集合 0 in s に対して、0 から出発して s の中を全域に動ける s の中の決め方
    dp2 = np.zeros(1 << N, np.int64)
    for s in range(1 << N):
        if not s & 1:
            continue
        x = pow2[dp1[s]]  # 全体
        t = s
        while t:
            t = (t - 1) & s
            if not t & 1:
                continue
            # s の中の辺を使ったときに、ちょうど可動域が t に一致する場合を求める
            y = dp2[t]
            e1 = dp1[s ^ t]  # 自由に決める
            e2 = dp1[s] - dp1[t] - e1  # 内向きに決めるしかない
            y = y * pow2[e1] % MOD
            x -= y
        dp2[s] = x % MOD
    # 部分集合 1 in s に対して、1 から出発して s の中を全域に動ける s の中に決め方
    dp3 = np.zeros(1 << N, np.int64)
    for s in range(1 << N):
        if not s & 2:
            continue
        x = pow2[dp1[s]]  # 全体
        t = s
        while t:
            t = (t - 1) & s
            if not t & 2:
                continue
            # s の中の辺を使ったときに、ちょうど可動域が t に一致する場合を求める
            y = dp3[t]
            e1 = dp1[s ^ t]  # 自由に決める
            e2 = dp1[s] - dp1[t] - e1  # 内向きに決めるしかない
            y = y * pow2[e1] % MOD
            x -= y
        dp3[s] = x % MOD

    # 答の計算をする
    full = (1 << N) - 1
    ans = pow2[dp1[full]]
    # 1 から出発していける集合がちょうど s
    for s in range(1 << N):
        sc = full ^ s
        if not s & 1:
            continue
        if not sc & 2:
            continue
        t = sc + 1
        while t:
            t = (t - 1) & sc
            if t & 2:
                u = full ^ s ^ t
                # (s,t)-edge の個数
                e = dp1[s | t] - dp1[s] - dp1[t]
                if e:
                    continue
                x = dp2[s] * dp3[t] % MOD  # s, t での決め方
                x = x * pow2[dp1[u]] % MOD  # u 内での決め方
                ans -= x
    return ans % MOD

N, M = map(int, readline().split())
G = np.zeros((N, N), np.int64)
for _ in range(M):
    a, b = map(int, readline().split())
    a, b = a - 1, b - 1
    G[a, b] = 1
    G[b, a] = 1

print(main(N, G))