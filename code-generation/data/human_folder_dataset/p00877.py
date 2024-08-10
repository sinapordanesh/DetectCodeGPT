from collections import defaultdict
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
    if C0 == C1 == 0:
        E0 = dot3(P0, P1, Q0)
        E1 = dot3(P0, P1, Q1)
        if not E0 < E1:
            E0, E1 = E1, E0
        return 0 <= E1 and E0 <= dist2(P0, P1)
    D0 = cross3(Q0, Q1, P0)
    D1 = cross3(Q0, Q1, P1)
    return C0 * C1 <= 0 and D0 * D1 <= 0

def convex_polygons_intersection(ps, qs):
    pl = len(ps); ql = len(qs)
    i = j = 0
    while (i < pl or j < ql) and (i < 2*pl) and (j < 2*ql):
        px0, py0 = ps0 = ps[(i-1)%pl]; px1, py1 = ps1 = ps[i%pl]
        qx0, qy0 = qs0 = qs[(j-1)%ql]; qx1, qy1 = qs1 = qs[j%ql]

        if is_intersection(ps0, ps1, qs0, qs1):
            return 1

        ax = px1 - px0; ay = py1 - py0
        bx = qx1 - qx0; by = qy1 - qy0

        v = (ax*by - bx*ay)
        va = cross3(qs0, qs1, ps1)
        vb = cross3(ps0, ps1, qs1)

        if v == 0 and va < 0 and vb < 0:
            return 0
        if v == 0 and va == 0 and vb == 0:
            i += 1
        elif v >= 0:
            if vb > 0:
                i += 1
            else:
                j += 1
        else:
            if va > 0:
                j += 1
            else:
                i += 1
    return 0

def convex_hull(ps):
    qs = []
    n = len(ps)
    for p in ps:
        while len(qs)>1 and cross3(qs[-1], qs[-2], p) >= 0:
            qs.pop()
        qs.append(p)
    t = len(qs)
    for i in range(n-2, -1, -1):
        p = ps[i]
        while len(qs)>t and cross3(qs[-1], qs[-2], p) >= 0:
            qs.pop()
        qs.append(p)
    return qs

def inside_convex_polygon(p0, qs):
    L = len(qs)
    left = 1; right = L
    q0 = qs[0]
    while left+1 < right:
        mid = (left + right) >> 1
        if cross3(q0, p0, qs[mid]) <= 0:
            left = mid
        else:
            right = mid
    if left == L-1:
        left -= 1
    qi = qs[left]; qj = qs[left+1]
    v0 = cross3(q0, qi, qj)
    v1 = cross3(q0, p0, qj)
    v2 = cross3(q0, qi, p0)
    if v0 < 0:
        v1 = -v1; v2 = -v2
    return 0 <= v1 and 0 <= v2 and v1 + v2 <= v0

def solve():
    N, M = map(int, readline().split())
    if N == M == 0:
        return False

    P = [list(map(int, readline().split())) for i in range(N)]
    Q = [list(map(int, readline().split())) for i in range(M)]

    P.sort()
    Q.sort()
    if N > 2:
        P = convex_hull(P)[:-1]
    if M > 2:
        Q = convex_hull(Q)[:-1]

    if N < 3 or M < 3:
        if not N < M:
            N, M = M, N
            P, Q = Q, P
        ok = 0
        if N == 1:
            if M == 1:
                ok = 1
            elif M == 2:
                ok = not is_intersection(P[0], P[0], Q[0], Q[1])
            else:
                ok = not inside_convex_polygon(P[0], Q)
        elif N == 2:
            if M == 2:
                ok = not is_intersection(P[0], P[1], Q[0], Q[1])
            else:
                ok = not (inside_convex_polygon(P[0], Q) or inside_convex_polygon(P[1], Q))
                for i in range(M):
                    ok &= not is_intersection(P[0], P[1], Q[i-1], Q[i])
        write("YES\n" if ok else "NO\n")
        return True


    if (convex_polygons_intersection(P, Q)
            or inside_convex_polygon(P[0], Q)
            or inside_convex_polygon(Q[0], P)):
        write("NO\n")
    else:
        write("YES\n")
    return True
while solve():
    ...
