from itertools import product
from sys import stdin, stdout

readline = stdin.readline
write = stdout.write

def dist2(x0, y0, z0, x1, y1, z1):
    return (x0 - x1)**2 + (y0 - y1)**2 + (z0 - z1)**2
def dot(x0, y0, z0, x1, y1, z1):
    return x0*x1 + y0*y1 + z0*z1
def cross2(x0, y0, z0, x1, y1, z1):
    return (y0*z1 - y1*z0)**2 + (z0*x1 - z1*x0)**2 + (x0*y1 - x1*y0)**2

while 1:
    N, M, R = map(int, readline().split())
    if N == M == R == 0:
        break
    S = [list(map(int, readline().split())) for i in range(N)]
    T = [list(map(int, readline().split())) for i in range(M)]

    ex, ey, ez = map(int, readline().split())
    S = [(sx - ex, sy - ey, sz - ez, sr) for sx, sy, sz, sr in S]
    T = [(tx - ex, ty - ey, tz - ez, tb) for tx, ty, tz, tb in T]
    L = [tb / (tx**2 + ty**2 + tz**2) for tx, ty, tz, tb in T]

    rem = [0]*M

    for i in range(M):
        tx, ty, tz, tb = T[i]
        ld = tx**2 + ty**2 + tz**2
        for j in range(N):
            sx, sy, sz, sr = S[j]
            sr2 = sr**2
            ok = 1
            dd1 = (sx**2 + sy**2 + sz**2 <= sr2)
            dd2 = (dist2(sx, sy, sz, tx, ty, tz) <= sr2)
            if dd1 ^ dd2:
                ok = 0
            elif dd1 == dd2 == 0:
                if (cross2(sx, sy, sz, tx, ty, tz) <= sr2 * ld):
                    if (dot(sx, sy, sz, tx, ty, tz) >= 0 and
                            dot(tx-sx, ty-sy, tz-sz, tx, ty, tz) >= 0):
                        ok = 0
            if not ok:
                rem[i] |= 1 << j
    ans = 0
    for P in product([0, 1], repeat=M):
        need = 0
        for i in range(M):
            if P[i]: need |= rem[i]
        if bin(need).count('1') <= R:
            ans = max(ans, sum(L[i] for i in range(M) if P[i]))
    write("%.10f\n" % ans)