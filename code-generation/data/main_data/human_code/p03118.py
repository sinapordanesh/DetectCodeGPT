import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 1_000_000_007

lim = 1 << 10
fact = np.ones(lim, np.int64)
for n in range(1, lim):
    fact[n] = fact[n - 1] * n % MOD
fact_inv = np.ones(lim, np.int64)
fact_inv[-1] = pow(int(fact[-1]), MOD - 2, MOD)
for n in range(lim - 1, 0, -1):
    fact_inv[n - 1] = n * fact_inv[n] % MOD
inv = np.zeros(lim, np.int64)
inv[1:] = fact[:-1] * fact_inv[1:] % MOD

def integrate_poly_0x(F):
    F1 = np.zeros_like(F)
    F1[1:] = F[:-1] * inv[1:len(F)] % MOD
    return F1

def integrate_poly_x1(F):
    F1 = -integrate_poly_0x(F)
    F1[0] -= F1.sum() % MOD
    return F1 % MOD

def integrate_0x(a, F, G):
    """\int_0^x (ae^{-x} + F(x) + G(x)/e)"""
    F1 = integrate_poly_0x(F)
    G1 = integrate_poly_0x(G)
    F1[0] += a
    return -a, F1, G1

def integrate_x1(a, F, G):
    """\int_x^1 (ae^{-x} + F(x) + G(x)/e)"""
    F1 = integrate_poly_x1(F)
    G1 = integrate_poly_x1(G)
    G1[0] -= a
    return a, F1, G1

def integrate_01(a, F, G):
    a, F, G = integrate_x1(a, F, G)
    F[1:] = 0
    G[1:] = 0
    F[0] += a
    return 0, F, G

def one_to_zero(dp0, dp1, dp2):
    dp0 = integrate_0x(*dp2)
    dp1 = integrate_x1(*dp2)
    dp2 = [0, np.zeros(N, np.int64), np.zeros(N, np.int64)]
    return dp0, dp1, dp2

def zero_to_one(dp0, dp1, dp2):
    a0, F0, G0 = integrate_01(*dp0)
    a1, F1, G1 = integrate_x1(*dp1)
    dp0 = [0, np.zeros(N, np.int64), np.zeros(N, np.int64)]
    dp1 = [0, np.zeros(N, np.int64), np.zeros(N, np.int64)]
    dp2 = [a0 + a1, F0 + F1, G0 + G1]
    return dp0, dp1, dp2

def zero_to_zero(dp0, dp1, dp2):
    a0, F0, G0 = integrate_01(*dp0)
    dp0 = [0, np.zeros(N, np.int64), np.zeros(N, np.int64)]
    dp1 = [a0, F0, G0]
    dp2 = [0, np.zeros(N, np.int64), np.zeros(N, np.int64)]
    return dp0, dp1, dp2

def integrate_poly_01_with_exp(F):
    # int_0^1 e^{-x}F(x)dx = a + b/e の計算
    a, b = 0, 0
    F = F.copy()
    while len(F) > 0:
        a += F[0]
        b -= F.sum() % MOD
        F = F[1:] * np.arange(1, len(F)) % MOD
    return a, b

def integrate_01_with_exp(a, F, G):
    # int_0^1 e^{-x}(ae^{-x}+F(x)+G(x)/e) = a + b/e +c/e^2の計算
    ans = np.zeros(3, np.int64)
    if a & 1:
        a += MOD
    ans[0] += a // 2
    ans[2] -= a // 2
    a, b = integrate_poly_01_with_exp(F)
    ans[0] += a
    ans[1] += b
    a, b = integrate_poly_01_with_exp(G)
    ans[1] += a
    ans[2] += b
    return ans % MOD

def get_ans(dp0, dp1, dp2):
    ans = np.zeros(3, np.int64)

    a, F, G = integrate_01(*dp0)
    ans[0] += a + F[0]
    ans[1] += G[0]
    a, F, G = integrate_01(*dp1)
    ans[0] += a + F[0]
    ans[1] += G[0]
    ans -= integrate_01_with_exp(*dp1)
    ans += integrate_01_with_exp(*dp2)
    ans %= MOD
    return ans

N = int(readline())
S = [1 if x == 'X' else 0 for x in readline().rstrip().decode()]
N += 10

dp0 = [0, np.zeros(N, np.int64), np.zeros(N, np.int64)]
dp1 = [0, np.zeros(N, np.int64), np.zeros(N, np.int64)]
dp2 = [0, np.zeros(N, np.int64), np.zeros(N, np.int64)]

if S[0] == 1:
    dp2[0] = 1
else:
    dp0[0] = -1
    dp0[1][0] = 1
    dp1[0] = 1
for s, t in zip(S, S[1:]):
    if (s, t) == (1, 1):
        print(0, 0, 0)
        exit()
    elif (s, t) == (1, 0):
        dp0, dp1, dp2 = one_to_zero(dp0, dp1, dp2)
    elif (s, t) == (0, 1):
        dp0, dp1, dp2 = zero_to_one(dp0, dp1, dp2)
    elif (s, t) == (0, 0):
        dp0, dp1, dp2 = zero_to_zero(dp0, dp1, dp2)
print(*get_ans(dp0, dp1, dp2))