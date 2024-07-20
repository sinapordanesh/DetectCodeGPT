from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N, M, K = map(int, readline().split())
    if N == 0:
        return False
    def root(x):
        if prt[x] == x:
            return x
        prt[x] = y = root(prt[x])
        return y
    def unite(x, y):
        px = root(x); py = root(y)
        if px == py:
            return 0
        if px < py:
            prt[py] = px
        else:
            prt[px] = py
        return 1
    E = []
    for i in range(M):
        u, v, w, l = readline().strip().split()
        u = int(u); v = int(v); w = int(w)
        if l == "A":
            E.append((w, u-1, v-1, 0))
        else:
            E.append((w, u-1, v-1, 1))
    E.sort()
    U = [0]*M
    cnt = 0; ec = 0
    ans = 0
    *prt, = range(N)
    for i, (w, u, v, d) in enumerate(E):
        if unite(u, v):
            U[i] = 1
            if d == 0:
                cnt += 1
            ec += 1
            ans += w
    if ec != N-1:
        write("-1\n")
        return True


    if cnt < K:
        m = 0
    else:
        m = 1

    que = deque()
    used = [0]*N; zeros = [0]*N

    G = [[] for i in range(N)]
    for i in range(M):
        if not U[i]:
            continue
        w, u, v, d = E[i]
        if d == m:
            G[u].append((v, 0, -1))
            G[v].append((u, 0, -1))
        else:
            G[u].append((v, w, i))
            G[v].append((u, w, i))

    for t in range(abs(K - cnt)):
        s = 10**18; p = q = -1
        for i in range(M):
            if U[i]:
                continue
            wi, ui, vi, di = E[i]
            if di != m:
                continue
            que.append((ui, 0, -1))
            used[:] = zeros
            used[ui] = 1
            while que:
                u, r, j = que.popleft()
                if u == vi:
                    wj = r
                    break
                for v, w, k in G[u]:
                    if used[v]:
                        continue
                    if k != -1 and r < w:
                        que.append((v, w, k))
                    else:
                        que.append((v, r, j))
                    used[v] = 1
            que.clear()
            if wi - wj < s and j != -1:
                s = wi - wj
                p = i; q = j
        if p == -1:
            write("-1\n")
            return True
        wq, uq, vq, dq = E[q]
        g = G[uq]
        for i in range(len(g)):
            if g[i][0] == vq:
                g.pop(i)
                break
        g = G[vq]
        for i in range(len(g)):
            if g[i][0] == uq:
                g.pop(i)
                break
        wp, up, vp, dp = E[p]
        G[up].append((vp, 0, -1))
        G[vp].append((up, 0, -1))
        U[p] = 1; U[q] = 0
        ans += s
    write("%d\n" % ans)
    return True
while solve():
    ...
