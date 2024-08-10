import sys
readline = sys.stdin.readline
write = sys.stdout.write

def stern_brocot(p, n):
    la = 0; lb = 1
    ra = 1; rb = 0
    lu = ru = 1
    lx = 0; ly = 1
    rx = 1; ry = 0
    while lu or ru:
        ma = la + ra; mb = lb + rb
        if p * mb**2 < ma**2:
            ra = ma; rb = mb
            if ma <= n and mb <= n:
                rx = ma; ry = mb
            else:
                lu = 0
        else:
            la = ma; lb = mb
            if ma <= n and mb <= n:
                lx = ma; ly = mb
            else:
                ru = 0
    return lx, ly, rx, ry

while 1:
    p, n = map(int, readline().split())
    if p == 0:
        break
    lx, ly, rx, ry = stern_brocot(p, n)
    write("%d/%d %d/%d\n" % (rx, ry, lx, ly))
