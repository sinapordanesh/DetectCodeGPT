from itertools import product
from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    MOD = 10**9 + 9
    N, M = map(int, readline().split())

    K = 3*N
    fact = [1]*(K+1)
    rfact = [1]*(K+1)
    r = 1
    for i in range(1, K+1):
        fact[i] = r = r * i % MOD
    rfact[K] = r = pow(fact[K], MOD-2, MOD)
    for i in range(K, 0, -1):
        rfact[i-1] = r = r * i % MOD

    pr6 = [1]*(N+1)
    base = pow(6, MOD-2, MOD)
    r = 1
    for i in range(N):
        pr6[i+1] = r = base * r % MOD

    mp = {}
    G = [[] for i in range(M*2)]
    cur = 0
    m = 0
    E = []
    for i in range(M):
        a, b, c = map(int, readline().split())
        if a not in mp:
            mp[a] = cur
            cur += 1
        ma = mp[a]
        if b not in mp:
            mp[b] = cur
            cur += 1
        mb = mp[b]
        if c == 0:
            G[ma].append(mb)
            G[mb].append(ma)
        else:
            E.append((ma, mb))
            m += 1
    L = cur
    cr = 0
    lb = [-1]*L
    sz = []
    zz = []
    cc = [0, 0, 0]
    u = [0]*L
    que = deque()
    for i in range(L):
        if u[i]:
            continue
        que.append(i)
        vs = []
        u[i] = 1
        while que:
            v = que.popleft()
            vs.append(v)
            for w in G[v]:
                if u[w]:
                    continue
                u[w] = 1
                que.append(w)
        s = len(vs)
        if s > 3:
            write("0\n")
            return
        for v in vs:
            lb[v] = cr
        sz.append(s)
        zz.append(vs)
        cc[s-1] += 1
        cr += 1
    used = [0]*(1 << m)
    ans = 0
    def dfs(state, c, lb, cc):
        nonlocal ans
        if used[state]:
            return
        used[state] = 1
        x = cc[0] + (K - L); y = cc[1]
        if x >= y:
            k = (x - y) // 3
            if c & 1 == 0:
                ans += fact[x] * pr6[k] * rfact[k] % MOD
            else:
                ans -= fact[x] * pr6[k] * rfact[k] % MOD
        cc0 = [0]*3
        for i in range(m):
            if state & (1 << i):
                continue
            p, q = E[i]
            pl = lb[p]; ql = lb[q]
            if pl != ql:
                s = sz[pl] + sz[ql]
                if s > 3:
                    continue
                cc0[:] = cc
                cc0[sz[pl]-1] -= 1
                cc0[sz[ql]-1] -= 1
                cc0[s-1] += 1

                nl = len(sz)
                vs = zz[pl] + zz[ql]
                for v in vs:
                    lb[v] = nl
                sz.append(s)
                zz.append(vs)

                dfs(state | (1 << i), c+1, lb, cc0)

                for v in zz[pl]:
                    lb[v] = pl
                for v in zz[ql]:
                    lb[v] = ql
            else:
                dfs(state | (1 << i), c+1, lb, cc)
    dfs(0, 0, lb, cc)
    ans %= MOD
    write("%d\n" % ans)
solve()
