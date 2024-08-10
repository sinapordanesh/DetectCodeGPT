from collections import defaultdict
import sys
def solve():
    readline = sys.stdin.readline
    write = sys.stdout.write
    mod = 10**9 + 9
    base = 37
    ca = ord('a')

    N = int(readline())
    SS = [readline().strip() for i in range(N)]
    SS.sort(key = len)

    T = readline().strip()
    L = len(T)

    L0 = max(max(map(len, SS)), L)

    r = 1
    pw = [1]*(L0+1)
    for i in range(L0):
        pw[i+1] = r = r * base % mod

    SM = defaultdict(dict)
    E = [None]*N
    for i in range(N):
        s = SS[i][::-1]
        h = 0
        p = -1
        for j, c in enumerate(s):
            h = (h + pw[j] * (ord(c) - ca)) % mod
            if j+1 in SM and h in SM[j+1]:
                p = SM[j+1][h]
        l = len(s)
        E[i] = (E[p] + [l]) if p != -1 else [l]
        SM[l][h] = i

    *SI, = SM.items()
    SI.sort()
    H = [0]*(L+1)
    r = 0
    for i, c in enumerate(T):
        H[i+1] = r = (base * r + (ord(c) - ca)) % mod

    MOD = 10**9 + 7
    dp = [0]*(L+1)
    dp[0] = 1
    SI.append((L+10, set()))
    it = iter(SI).__next__
    ln, sn = it()
    SL = []
    for i in range(1, L+1):
        if i == ln:
            SL.append((ln, sn, pw[ln]))
            ln, sn = it()
        hi = H[i]
        for l, hs, w in reversed(SL):
            v = (hi - H[i-l]*w) % mod
            if v in hs:
                dp[i] = sum(dp[i-e] for e in E[hs[v]]) % MOD
                break
    write("%d\n" % dp[L])
solve()
