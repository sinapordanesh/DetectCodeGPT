import sys
readline = sys.stdin.readline
write = sys.stdout.write

def cross_point(p0, q0, p1, q1):
    x0, y0 = p0; x1, y1 = q0
    x2, y2 = p1; x3, y3 = q1
    dx0 = x1 - x0
    dy0 = y1 - y0
    dx1 = x3 - x2
    dy1 = y3 - y2

    s = (y0-y2)*dx1 - (x0-x2)*dy1
    sm = dx0*dy1 - dy0*dx1
    if sm == 0:
        return None
    return x0 + s*dx0/sm, y0 + s*dy0/sm

def solve():
    W, H, N, R = map(int, readline().split())
    if W == H == 0:
        return False
    L = [tuple(map(int, readline().split())) for i in range(N)]
    L.extend([
        (0, 0, W, 0, 0),
        (0, 0, 0, H, 0),
        (0, H, W, H, 0),
        (W, 0, W, H, 0),
    ])
    EPS = 1e-9
    pp = ((1, 1), (1, -1), (-1, 1), (-1, -1))
    for i in range(N+4):
        xi1, yi1, xi2, yi2, t0 = L[i]
        p0 = (xi1, yi1); q0 = (xi2, yi2)
        dx0 = (xi2 - xi1); dy0 = (yi2 - yi1)
        d0 = (dx0**2 + dy0**2)**.5
        for j in range(i):
            xj1, yj1, xj2, yj2, t1 = L[j]
            p1 = (xj1, yj1); q1 = (xj2, yj2)
            dx1 = (xj2 - xj1); dy1 = (yj2 - yj1)
            d1 = (dx1**2 + dy1**2)**.5
            cp = cross_point(p0, q0, p1, q1)
            if cp is None:
                continue
            x0, y0 = cp
            sv = abs(dx0*dy1 - dx1*dy0)
            for p, q in pp:
                a = p*d1*(t1+R)
                b = q*d0*(t0+R)
                x = x0 + (a * dx0 + b * dx1) / sv
                y = y0 + (a * dy0 + b * dy1) / sv
                if not R - EPS < x < W-R + EPS or not R - EPS < y < H-R + EPS:
                    continue
                ok = 1
                for k in range(N):
                    xk1, yk1, xk2, yk2, t2 = L[k]
                    dxp = xk2 - xk1; dyp = yk2 - yk1
                    dxq = x - xk1; dyq = y - yk1
                    d2 = (dxp**2 + dyp**2)**.5
                    if abs(dxp*dyq - dxq*dyp) < (R + t2) * d2 - EPS:
                        ok = 0
                if ok:
                    write("Yes\n")
                    return True
    write("No\n")
    return True
while solve():
    ...
