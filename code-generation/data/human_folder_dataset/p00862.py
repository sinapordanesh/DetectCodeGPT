import sys
readline = sys.stdin.readline
write = sys.stdout.write

def cross2(p, q):
    return p[0]*q[1] - p[1]*q[0]
def cross3(o, p, q):
    return (p[0] - o[0])*(q[1] - o[1]) - (p[1] - o[1])*(q[0] - o[0])
def dot2(p, q):
    return p[0]*q[0] + p[1]*q[1]
def dist2(p):
    return p[0]**2 + p[1]**2
def segment_line_dist(x, p0, p1):
    z0 = (p1[0] - p0[0], p1[1] - p0[1])
    z1 = (x[0] - p0[0], x[1] - p0[1])
    if 0 <= dot2(z0, z1) <= dist2(z0):
        return abs(cross2(z0, z1)) / dist2(z0)**.5
    z2 = (x[0] - p1[0], x[1] - p1[1])
    return min(dist2(z1), dist2(z2))**.5

def polygon_cont(x, PS):
    V = [cross3(PS[i-1], PS[i], x) for i in range(len(PS))]
    return all(e >= 0 for e in V) or all(e <= 0 for e in V)
def polygon_dist(x, PS):
    return min(segment_line_dist(x, PS[i-1], PS[i]) for i in range(len(PS)))

def check(x, PS):
    if not polygon_cont(x, PS):
        return -polygon_dist(x, PS)
    return polygon_dist(x, PS)
def check_x(x, PS):
    ly = min(y for x, y in PS); ry = max(y for x, y in PS)
    EPS = 1e-6
    while ly + EPS < ry:
        y0 = (ly*2 + ry) / 3; y1 = (ly + ry*2) / 3
        if check((x, y0), PS) < check((x, y1), PS):
            ly = y0
        else:
            ry = y1
    return ly

def solve():
    N = int(readline())
    if N == 0:
        return False
    PS = [list(map(int, readline().split())) for i in range(N)]
    EPS = 1e-6
    lx = min(x for x, y in PS); rx = max(x for x, y in PS)
    while lx + EPS < rx:
        x0 = (lx*2 + rx) / 3; x1 = (lx + rx*2) / 3
        y0 = check_x(x0, PS); y1 = check_x(x1, PS)
        if check((x0, y0), PS) < check((x1, y1), PS):
            lx = x0
        else:
            rx = x1
    x0 = lx
    y0 = check_x(x0, PS)
    write("%.16f\n" % check((x0, y0), PS))
    return True
while solve():
    ...
