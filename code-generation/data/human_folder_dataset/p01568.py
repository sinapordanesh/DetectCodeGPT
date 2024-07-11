from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def dot3(O, A, B):
    ox, oy = O; ax, ay = A; bx, by = B
    return (ax - ox) * (bx - ox) + (ay - oy) * (by - oy)
def cross3(O, A, B):
    ox, oy = O; ax, ay = A; bx, by = B
    return (ax - ox) * (by - oy) - (bx - ox) * (ay - oy)
def dist2(A, B):
    ax, ay = A; bx, by = B
    return (ax - bx) ** 2 + (ay - by) ** 2
def is_intersection(L1, L2):
    P0 = L1[:2]; P1 = L1[2:]
    Q0 = L2[:2]; Q1 = L2[2:]
    C0 = cross3(P0, P1, Q0)
    C1 = cross3(P0, P1, Q1)
    D0 = cross3(Q0, Q1, P0)
    D1 = cross3(Q0, Q1, P1)
    if C0 == C1 == 0:
        return False
    return C0 * C1 <= 0 and D0 * D1 <= 0
def cross_point(L1, L2):
    x0, y0, x1, y1 = L1
    x2, y2, x3, y3 = L2
    dx0 = x1 - x0
    dy0 = y1 - y0
    dx1 = x3 - x2
    dy1 = y3 - y2

    s = (y0-y2)*dx1 - (x0-x2)*dy1
    sm = dx0*dy1 - dy0*dx1
    if s < 0:
        s = -s
        sm = -sm
    if s == 0:
        x = x0; y = y0
    elif s == sm:
        x = x1; y = y1
    else:
        x = x0 + s*dx0/sm; y = y0 + s*dy0/sm
    return x, y
def solve():
    N, M = map(int, readline().split())
    ps = set()
    mp = {}
    LS = []
    for i in range(N):
        x1, y1, x2, y2 = map(int, readline().split())
        mp[x1, y1] = 0
        mp[x2, y2] = 0
        LS.append((x1, y1, x2, y2))
    for i in range(N):
        L1 = LS[i]
        for j in range(i+1, N):
            L2 = LS[j]
            if is_intersection(L1, L2):
                x, y = cross_point(L1, L2)
                mp[x, y] = 0

    for i in range(M):
        x, y = map(int, readline().split())
        mp[x, y] = 1
    xb, yb = map(int, readline().split())
    mp[xb, yb] = 2
    xc, yc = map(int, readline().split())
    mp[xc, yc] = 2

    *ps1, = mp.keys()
    ps1.sort(key = lambda x: (x[0], x[1]))
    mv = {e: i for i, e in enumerate(ps1)}
    *ps2, = mp.keys()
    ps2.sort(key = lambda x: (x[1], x[0]))

    ES = []
    ms = list(map(mv.__getitem__, ps2))
    ks = list(map(mp.__getitem__, ps1))
    K = len(ps1)
    G = [[] for i in range(K)]
    for x1, y1, x2, y2 in LS:
        vs = []
        if x1 != x2:
            if not x1 <= x2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            for k, (x, y) in enumerate(ps1):
                if x1 <= x <= x2 and abs((x - x1)*(y2 - y1) - (y - y1)*(x2 - x1)) < 1e-6:
                    vs.append(k)
        else:
            if not y1 <= y2:
                y1, y2 = y2, y1
            for k, (x, y) in zip(ms, ps2):
                if y1 <= y <= y2 and abs((x - x1)*(y2 - y1) - (y - y1)*(x2 - x1)) < 1e-6:
                    vs.append(k)
        for i in range(len(vs)-1):
            k1 = vs[i]; k2 = vs[i+1]
            G[k1].append(k2)
            G[k2].append(k1)
            ES.append((k1, k2) if k1 <= k2 else (k2, k1))
    s = mv[xc, yc]; t = mv[xb, yb]
    que = deque([s])
    used = [0]*K
    used[s] = 1
    e_used = set()
    while que:
        v = que.popleft()
        for w in G[v]:
            if w == t:
                write("-1\n")
                return
            e_used.add((v, w) if v <= w else (w, v))
            if not used[w] and ks[w] != 1:
                que.append(w)
            used[w] = 1
    que.append(t)
    e_used1 = set()
    used = [0]*K
    used[t] = 1
    while que:
        v = que.popleft()
        for w in G[v]:
            e = (v, w) if v <= w else (w, v)
            if e in e_used:
                continue
            e_used1.add(e)
            if not used[w]:
                que.append(w)
                used[w] = 1
    ans = 0
    for k1, k2 in ES:
        if (k1, k2) in e_used1:
            continue
        x1, y1 = ps1[k1]; x2, y2 = ps1[k2]
        ans += ((x1 - x2)**2 + (y1 - y2)**2)**.5
    write("%.16f\n" % ans)
solve()
