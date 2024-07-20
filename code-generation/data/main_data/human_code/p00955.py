from math import sqrt, atan2
def intersection01(cx, cy, r, x1, y1, x2, y2):
    xd = x2 - x1; yd = y2 - y1
    X = x1 - cx; Y = y1 - cy
    a = xd**2 + yd**2
    b = xd * X + yd * Y
    c = X**2 + Y**2 - r**2
    D = b**2 - a*c
    result = []
    if D > 0:
        d = sqrt(D)
        if 0 < -b - d < a:
            s = (-b - d) / a
            result.append((x1 + xd*s, y1 + yd*s))
        if 0 < -b + d < a:
            s = (-b + d) / a
            result.append((x1 + xd*s, y1 + yd*s))
    elif D == 0:
        if 0 < -b < a:
            s = -b / a
            result.append((x1 + xd*s, y1 + yd*s))
    return result
def calc(x0, y0, x1, y1, rr):
    if x0**2 + y0**2 - rr <= 1e-8 and x1**2 + y1**2 - rr <= 1e-8:
        return (x0 * y1 - x1 * y0) / 2.
    theta = atan2(x0*y1 - x1*y0, x0*x1 + y0*y1)
    return theta*rr/2.

n, r = map(int, input().split())
P = [list(map(int, input().split())) for i in range(n)]

rr = r**2
def solve(xb, yb):
    ans = 0
    for i in range(n):
        x0, y0 = P[i-1]; x1, y1 = P[i]
        x0 -= xb; y0 -= yb
        x1 -= xb; y1 -= yb
        result = intersection01(0, 0, r, x0, y0, x1, y1)
        px = x0; py = y0
        for x, y in result:
            ans += calc(px, py, x, y, rr)
            px = x; py = y
        ans += calc(px, py, x1, y1, rr)
    return ans

x0 = sum(x for x, y in P)/n
y0 = sum(y for x, y in P)/n
ans = solve(x0, y0)
import random
random.seed()
randint = random.randint
for i in range(1000):
    ma = ans; nxt = None
    for j in range(100):
        dx = randint(-1000000, 1000000) / 10000 / (i+1)
        dy = randint(-1000000, 1000000) / 10000 / (i+1)
        res = solve(x0 + dx, y0 + dy)
        if ma < res:
            ma = res
            nxt = (x0 + dx, y0 + dy)
    if nxt is not None:
        ans = ma
        x0, y0 = nxt
print(ans)