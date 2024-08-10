from heapq import heappush, heappop
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N, T, R = map(int, readline().split())
    if N == T == R == 0:
        return False
    S = [None]*N
    TS = [None]*N
    for i in range(N):
        s = readline().strip()
        S[i] = s
        prv, x0, y0 = map(int, readline().split())
        r = []
        while prv != T:
            t, vx, vy = map(int, readline().split())
            r.append((prv, t, x0, y0, vx, vy))
            x0 += vx*(t - prv); y0 += vy*(t - prv)
            prv = t
        TS[i] = r
    INF = 10**18
    que = [(0, 0)]
    dist = [INF]*N
    dist[0] = 0
    while que:
        cost, v = heappop(que)
        if cost - dist[v] > 1e-6:
            continue
        k0 = 0
        T1 = TS[v]
        while 1:
            t0, t1, x0, y0, vx, vy = T1[k0]
            if t0 <= cost <= t1:
                break
            k0 += 1
        for w in range(N):
            if v == w or dist[w] < cost:
                continue
            k1 = k0
            k2 = 0
            T2 = TS[w]
            while 1:
                t0, t1, x0, y0, vx, vy = T2[k2]
                if t0 <= cost <= t1:
                    break
                k2 += 1
            while 1:
                p0, p1, x0, y0, vx0, vy0 = T1[k1]
                q0, q1, x1, y1, vx1, vy1 = T2[k2]
                t0 = max(p0, q0, cost); t1 = min(p1, q1)
                if dist[w] <= t0:
                    break
                a0 = (vx0 - vx1)
                a1 = (x0 - p0*vx0) - (x1 - q0*vx1)
                b0 = (vy0 - vy1)
                b1 = (y0 - p0*vy0) - (y1 - q0*vy1)
                A = a0**2 + b0**2
                B = 2*(a0*a1 + b0*b1)
                C = a1**2 + b1**2 - R**2
                if A == 0:
                    assert B == 0
                    if C <= 0:
                        e = t0
                        if e < dist[w]:
                            dist[w] = e
                            heappush(que, (e, w))
                        break
                else:
                    D = B**2 - 4*A*C
                    if D >= 0:
                        s0 = (-B - D**.5) / (2*A)
                        s1 = (-B + D**.5) / (2*A)
                        if t0 <= s1 and s0 <= t1:
                            e = max(t0, s0)
                            if e < dist[w]:
                                dist[w] = e
                                heappush(que, (e, w))
                            break
                if p1 < q1:
                    k1 += 1
                elif p1 > q1:
                    k2 += 1
                elif p1 == T:
                    break
                else:
                    k1 += 1; k2 += 1
    ans = []
    for i in range(N):
        if dist[i] < INF:
            ans.append(S[i])
    ans.sort()
    for e in ans:
        write("%s\n" % e)
    return True
while solve():
    ...
