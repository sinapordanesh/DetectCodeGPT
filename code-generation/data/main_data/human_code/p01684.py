import sys
readline = sys.stdin.readline
write = sys.stdout.write

from math import pi, sqrt, acos, sin

def solve():
    EPS = 1e-9
    W, H, A, B, C = map(int, readline().split())
    if W == 0:
        return False
    a = sqrt(A / pi); b = sqrt(B / pi)
    mx = max(a, b)
    if 2*mx > min(W, H) - EPS:
        write("impossible\n")
        return True

    def calc(a, b, S):
        EPS = 1e-8
        left = abs(a-b) + EPS; right = a+b - EPS
        while left + EPS < right:
            mid = (left + right) / 2
            s = 0
            #print(a, b, mid, (a**2 + mid**2 - b**2) / (2*a*mid), (b**2 + mid**2 - a**2) / (2*b*mid))
            ta = acos((a**2 + mid**2 - b**2) / (2*a*mid))
            tb = acos((b**2 + mid**2 - a**2) / (2*b*mid))
            s = ((2*ta - sin(2*ta)) * a**2 + (2*tb - sin(2*tb)) * b**2) / 2
            if s < S:
                right = mid
            else:
                left = mid
        return right

    d0 = calc(a, b, C)
    e0 = abs(a - b)
    if e0 - EPS < d0:
        dx = W - a - b
        dy = H - a - b
        d1 = sqrt(dx**2 + dy**2)
        ax = ay = a; bx = a+dx*d0/d1; by = a+dy*d0/d1
        if bx-b < 0:
            ax -= bx-b; bx = b
        if by-b < 0:
            ay -= by-b; by = b
        if d0 < d1:
            write("%.16f %.16f %.16f %.16f %.16f %.16f\n" % (ax, ay, a, bx, by, b))
        else:
            write("impossible\n")
    else:
        write("%.16f %.16f %.16f %.16f %.16f %.16f\n" % (mx, mx, a, mx, mx, b))
    return True
while solve():
    ...
