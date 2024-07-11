import sys
readline = sys.stdin.readline
write = sys.stdout.write

EPS = 1e-9
def line_cross_point(P1, P2, Q1, Q2):
    x0, y0 = P1; x1, y1 = P2
    x2, y2 = Q1; x3, y3 = Q2

    dx0 = x1 - x0; dy0 = y1 - y0
    dx1 = x3 - x2; dy1 = y3 - y2

    s = (y0-y2)*dx1 - (x0-x2)*dy1
    sm = dx0*dy1 - dy0*dx1
    if -EPS < sm < EPS:
        return None
    return x0 + s*dx0/sm, y0 + s*dy0/sm

def bisector(P1, P2, Q1, Q2):
    x0, y0 = P1; x1, y1 = P2
    x2, y2 = Q1; x3, y3 = Q2

    dx0 = x1 - x0; dy0 = y1 - y0
    dx1 = x3 - x2; dy1 = y3 - y2

    cp = line_cross_point(P1, P2, Q1, Q2)
    if cp is None:
        return None

    cx, cy = cp

    d0 = (dx0**2 + dy0**2)**.5
    d1 = (dx1**2 + dy1**2)**.5
    return [
        ((cx, cy), (cx + (dx0*d1 + dx1*d0), cy + (dy0*d1 + dy1*d0))),
        ((cx, cy), (cx + (dx0*d1 - dx1*d0), cy + (dy0*d1 - dy1*d0))),
    ]

def line_point_dist2(p1, p2, q):
    x, y = q

    x1, y1 = p1; x2, y2 = p2
    dx = x2 - x1; dy = y2 - y1
    dd = dx**2 + dy**2
    sv = (x - x1) * dy - (y - y1) * dx
    return abs(sv / dd**.5)


def check(LS, q):
    ds = [line_point_dist2(p1, p2, q) for p1, p2 in LS]
    return all(abs(ds[0] - e) < EPS for e in ds)

def solve():
    N = int(readline())
    if N == 0:
        return False
    P = []
    for i in range(N):
        x1, y1, x2, y2 = map(int, readline().split())
        P.append(((x1, y1), (x2, y2)))
    if N <= 2:
        write("Many\n")
        return True

    s = []
    for i in range(N):
        p1, p2 = P[i]
        for j in range(i):
            q1, q2 = P[j]
            bs = bisector(p1, p2, q1, q2)
            if bs is None:
                continue
            s.append(bs)
            if len(s) > 1:
                break
        else:
            continue
        break
    if len(s) < 2:
        write("None\n")
        return True
    ans = []
    b1, b2 = s
    for p1, p2 in b1:
        for q1, q2 in b2:
            cp = line_cross_point(p1, p2, q1, q2)
            if cp is None:
                continue
            if check(P, cp):
                cx, cy = cp
                for ax, ay in ans:
                    if abs(cx - ax) < EPS and abs(cy - ay) < EPS:
                        break
                else:
                    ans.append(cp)
    if len(ans) == 0:
        write("None\n")
    elif len(ans) > 1:
        write("Many\n")
    else:
        write("%.16f %.16f\n" % ans[0])
    return True
while solve():
    ...
