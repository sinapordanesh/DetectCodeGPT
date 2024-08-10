# 75

import sys
sys.setrecursionlimit(10**8)

MOD = 10**9+7
N = int(input())
g_l = [[] for i in range(N)]
check_l = [-1] * N
num_l = [0] * N
for i in range(N-1):
    ai, bi = map(int, input().split())
    g_l[ai-1].append(bi-1)
    g_l[bi-1].append(ai-1)


def dfs(n):
    d = 1
    if check_l[n] > 0:
        return num_l[n]
    check_l[n] = 1
    for next_n in g_l[n]:
        d += dfs(next_n)
    num_l[n] = d
    return d


def modinv(a):
    # calc : (a**(-1)) %MOD
    return pow(a, MOD-2, MOD)


def solve():
    dfs(0)
    pow_l = [None]*(N+1)
    pow_l[0] = 1
    for i in range(1, N+1):
        pow_l[i] = (pow_l[i-1] * 2) % MOD

    ans = 0
    # for i in range(1, N):
    #     ans += (1 - (1/2)**num_l[i]) * (1 - (1/2)**(N-num_l[i]))
    # ans += 1 - (1/2)**N  # 辺の期待値→頂点の期待値に変換(空集合以外は+1される)
    # ans -= N/2  # 黒点の期待値を引く
    for i in range(1, N):
        ans = (ans + (pow_l[num_l[i]]-1) *
               (pow_l[N-num_l[i]]-1) % MOD) % MOD
    ans = (ans + (pow_l[N] - 1) - (N * pow_l[N-1]) % MOD) % MOD
    y = ans
    x = pow(2, N, MOD)

    z = (y * modinv(x)) % MOD

    print(z)


solve()
