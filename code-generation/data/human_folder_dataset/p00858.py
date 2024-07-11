from heapq import heappush, heappop
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
def is_intersection(P0, P1, Q0, Q1):
    C0 = cross3(P0, P1, Q0)
    C1 = cross3(P0, P1, Q1)
    D0 = cross3(Q0, Q1, P0)
    D1 = cross3(Q0, Q1, P1)
    if C0 == C1 == 0:
        E0 = dot3(P0, P1, Q0)
        E1 = dot3(P0, P1, Q1)
        if not E0 < E1:
            E0, E1 = E1, E0
        return E0 <= dist2(P0, P1) and 0 <= E1
    return C0 * C1 <= 0 and D0 * D1 <= 0

def solve():
    N = int(readline())
    if N == 0:
        return False
    sx, sy = map(int, readline().split())
    gx, gy = map(int, readline().split())
    P = []
    for i in range(N):
        x0, y0, x1, y1 = map(int, readline().split())
        p0 = (x0, y0); p1 = (x1, y1)
        P.append((p0, p1))
    def check(p0, p1, q):
        x1, y1 = p0; x2, y2 = p1
        x, y = q
        xd = (x2 - x1); yd = (y2 - y1)
        if (x - x1) * yd != (y - y1) * xd:
            return False
        if xd != 0:
            if xd < 0:
                return xd <= (x - x1) <= 0
            return 0 <= (x - x1) <= xd
        if yd < 0:
            return yd <= (y - y1) <= 0
        return 0 <= (y - y1) <= yd
    def calc(p0, p1, q):
        x1, y1 = p0; x2, y2 = p1
        x, y = q
        xd = (x2 - x1); yd = (y2 - y1)
        if (x - x1) * yd != (y - y1) * xd:
            return None
        if xd != 0:
            if xd < 0:
                return -(x - x1), -xd
            return (x - x1), xd
        if yd < 0:
            return -(y - y1), -yd
        return (y - y1), yd
    ss = set()
    G0 = [[] for i in range(N)]
    Q = [0]*N
    for i in range(N):
        pi, qi = P[i]
        u0 = u1 = 0
        for j in range(N):
            if i == j:
                continue
            pj, qj = P[j]
            if check(pj, qj, pi):
                u0 = 1
                G0[i].append(j)
            elif check(pj, qj, qi):
                u1 = 1
                G0[i].append(j)
        if u0 and u1:
            Q[i] = 1
            ss.add(pi)
            ss.add(qi)

    ss0 = sorted(ss)
    mp = {e: i for i, e in enumerate(ss0)}
    L = len(ss0)
    G = [[] for i in range(L)]

    for i in range(N):
        pi, qi = P[i]
        if not Q[i]:
            continue
        x0, y0 = pi; x1, y1 = qi
        E = [(0, 0, pi), (1, 0, qi)]
        for j in range(N):
            pj, qj = P[j]
            k = calc(pi, qi, pj)
            if k is not None:
                s0, t0 = k
                if 0 <= s0 <= t0:
                    if Q[j]:
                        E.append((s0/t0, 0, pj))
                    else:
                        x2, y2 = pj; x3, y3 = qj
                        E.append((s0/t0, 1, (x1 - x0)*(x3 - x2) + (y1 - y0)*(y3 - y2)))
            else:
                k = calc(pi, qi, qj)
                if k is not None:
                    s0, t0 = k
                    if 0 <= s0 <= t0:
                        if Q[j]:
                            E.append((s0/t0, 0, qj))
                        else:
                            x2, y2 = qj; x3, y3 = pj
                            E.append((s0/t0, 1, (x1 - x0)*(x3 - x2) + (y1 - y0)*(y3 - y2)))
        E.sort()
        pr = None
        a = b = 1
        for e, t, v in E:
            if t:
                if v < 0:
                    b = 0
                elif v > 0:
                    a = 0
                else:
                    a = b = 0
                continue
            if pr is not None and pr != v:
                d = dist2(pr, v)**.5
                k0 = mp[pr]; k1 = mp[v]
                if a:
                    G[k0].append((k1, d))
                if b:
                    G[k1].append((k0, d))
                a = b = 1
            pr = v

    INF = 10**18
    prv = [-1]*L
    dst = [INF]*L
    sp = mp[sx, sy]
    gp = mp[gx, gy]
    dst[sp] = 0
    que = [(0, sp)]
    while que:
        cost, v = heappop(que)
        if dst[v] < cost:
            continue
        for w, d in G[v]:
            if cost + d < dst[w]:
                dst[w] = cost + d
                prv[w] = v
                heappush(que, (cost + d, w))

    if dst[gp] == INF:
        write("-1\n")
        return True

    ans = []
    v = gp
    while v != sp:
        ans.append(ss0[v])
        v = prv[v]
    ans.append(ss0[v])
    ans.reverse()
    for x, y in ans:
        write("%d %d\n" % (x, y))
    write("0\n")
    return True
while solve():
    ...
