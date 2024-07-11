import sys
import numpy as np
import numba
from numba import njit
i8 = numba.int64

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 10**9 + 7

@njit((i8, ), cache=True)
def fact_table(N):
    inv = np.empty(N, np.int64)
    inv[0] = 0
    inv[1] = 1
    for n in range(2, N):
        q, r = divmod(MOD, n)
        inv[n] = inv[r] * (-q) % MOD
    fact = np.empty(N, np.int64)
    fact[0] = 1
    for n in range(1, N):
        fact[n] = n * fact[n - 1] % MOD
    fact_inv = np.empty(N, np.int64)
    fact_inv[0] = 1
    for n in range(1, N):
        fact_inv[n] = fact_inv[n - 1] * inv[n] % MOD
    return fact, fact_inv, inv

@njit((i8[::1], ), cache=True)
def main(A):
    # key：サイクルに選んだ個数、(d-2)の和
    # value：選んでいないもの：1/(d-1)!、選んだもの：1/(d-2)! の積の和
    N = len(A)
    U = N + 10
    dp = np.zeros((U, U), np.int64)
    dp[0, 0] = 1
    fact, fact_inv, inv = fact_table(10**3)
    if np.all(A == 2):
        return fact[N - 1] * inv[2] % MOD
    for d in A:
        newdp = np.zeros_like(dp)
        # 選ばない場合の遷移
        newdp += dp * fact_inv[d - 1] % MOD
        # 選ぶ場合の遷移
        if d >= 2:
            newdp[1:, d - 2:U] += dp[:-1, 0:U + 2 - d] * fact_inv[d - 2] % MOD
        dp = newdp % MOD
    ret = 0
    for n in range(3, N + 1):
        for a in range(N + 1):
            x = a * fact[n - 1] % MOD * fact[N - n - 1] % MOD
            x = x * inv[2] % MOD * dp[n, a] % MOD
            ret += x
    return ret % MOD

A = np.array(read().split(), np.int64)[1:]
print(main(A))