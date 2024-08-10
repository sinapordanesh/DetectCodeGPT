from heapq import heappush, heappop
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N = int(readline())
    if N == 0:
        return False
    P = [tuple(map(int, readline().split())) for i in range(N)]
    YS = set(y for x, y in P)
    Q = P[:]
    for i in range(N-1):
        x0, y0 = P[i]; x1, y1 = P[i+1]
        if y0 != y1:
            for y in YS:
                if y0 < y < y1 or y1 < y < y0:
                    x = (x1 - x0)/(y1 - y0)*(y - y0) + x0
                    assert x0 < x < x1 or x1 < x < x0
                    Q.append((x, y))
    Q.sort()
    def f(px, py, qx, qy):
        if py == qy:
            return abs(px - qx)
        return ((px - qx)**2 + (py - qy)**2)**.5
    L = len(Q)
    INF = 10**18
    que = [(0, 0, L-1)]
    dist = {(0, L-1): 0}
    dd = ((1, -1), (1, 0), (0, -1), (-1, 0), (0, 1), (1, 1), (-1, -1), (-1, 1))
    while que:
        cost, a, b = heappop(que)
        if cost < dist[a, b]:
            continue
        if a == b:
            write("%.16f\n" % cost)
            break
        ax, ay = Q[a]; bx, by = Q[b]
        for da, db in dd:
            na = a + da; nb = b + db
            if not 0 <= na <= nb < L:
                continue
            cx, cy = Q[na]; dx, dy = Q[nb]
            if cy != dy:
                continue
            n_cost = cost + f(ax, ay, cx, cy) + f(bx, by, dx, dy)
            key = (na, nb)
            if n_cost < dist.get(key, INF):
                dist[key] = n_cost
                heappush(que, (n_cost, na, nb))
    else:
        write("-1\n")
    return True
while solve():
    ...
