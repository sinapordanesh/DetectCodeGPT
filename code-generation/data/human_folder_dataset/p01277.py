from collections import defaultdict
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def gcd(m, n):
    while n:
        m, n = n, m % n
    return m
def solve():
    N = int(readline())
    P = [list(map(int, readline().split())) for i in range(N)]
    ok = 0
    x0, y0 = P[0]; x1, y1 = P[1]
    for i in range(2, N):
        x2, y2 = P[i]
        if (x1 - x0) * (y2 - y0) != (x2 - x0) * (y1 - y0):
            ok = 1
            break
    if not ok:
        write("No\n")
        return
    A = defaultdict(int)
    B = defaultdict(int)
    for i in range(N):
        xi, yi = P[i]
        for j in range(i):
            xj, yj = P[j]
            dx = xi - xj; dy = yi - yj
            g = gcd(abs(dx), abs(dy))
            dx //= g; dy //= g
            if dy < 0:
                dx = -dx; dy = -dy
            if dx == 0:
                p = xi * dy - yi * dx; q = dy
                g = gcd(abs(p), abs(q))
                p //= g; q //= g
                if q < 0:
                    q = -q; p = -p
                key = (p, 0, q, dx, dy)
            else:
                p = yi * dx - xi * dy; q = dx
                g = gcd(abs(p), abs(q))
                p //= g; q //= g
                if q < 0:
                    q = -q; p = -p
                key = (0, p, q, dx, dy)
            A[key] += 1

            gx = -dy; gy = dx
            if gy < 0:
                gx = -gx; gy = -gy
            if dy == 0:
                p = dy * (yi + yj) + dx * (xi + xj)
                q = 2 * dx
                g = gcd(abs(p), abs(q))
                p //= g; q //= g
                if q < 0:
                    q = -q; p = -p
                key = (p, 0, q, gx, gy)
            else:
                p = dx * (xi + xj) + dy * (yi + yj)
                q = 2 * dy
                g = gcd(abs(p), abs(q))
                p //= g; q //= g
                if q < 0:
                    q = -q; p = -p
                key = (0, p, q, gx, gy)
            B[key] += 1
    ok = 0
    if N % 2 == 0:
        for k, v in B.items():
            if 2*v == N:
                ok = 1
                break
            if 2*v == N-2:
                if A[k] == 1:
                    ok = 1
                    break
    else:
        R = []
        for k, v in B.items():
            if 2*v+1 == N:
                R.append(k)
        ok = 0
        for x0, y0, z0, dx, dy in R:
            cnt = 0
            for x, y in P:
                if dy*(x*z0 - x0) == dx*(y*z0 - y0):
                    cnt += 1
            if cnt == 1:
                ok = 1
                break
    if ok:
        write("Yes\n")
    else:
        write("No\n")
solve()
