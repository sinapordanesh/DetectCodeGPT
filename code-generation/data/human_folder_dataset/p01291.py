from heapq import heappush, heappop
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def cross2(p, q):
    return p[0]*q[1] - p[1]*q[0]
def dot2(p, q):
    return p[0]*q[0] + p[1]*q[1]
def dist2(p):
    return p[0]**2 + p[1]**2
def segment_line_dist(x, p0, p1):
    z0 = (p1[0] - p0[0], p1[1] - p0[1])
    z1 = (x[0] - p0[0], x[1] - p0[1])
    if 0 <= dot2(z0, z1) <= dist2(z0):
        return cross2(z0, z1)**2 / dist2(z0)
    z2 = (x[0] - p1[0], x[1] - p1[1])
    return min(dist2(z1), dist2(z2))

def solve():
    W, N = map(int, readline().split())
    if W == N == 0:
        return False
    PS = []
    for i in range(N):
        M = int(readline())
        P = [list(map(int, readline().split())) for i in range(M)]
        PS.append(P)

    G = [[] for i in range(N+2)]
    for i in range(N):
        Pi = PS[i]
        ni = len(Pi)
        for j in range(i+1, N):
            Pj = PS[j]
            r = 10**18
            nj = len(Pj)
            for p1 in Pi:
                for k in range(nj):
                    q1 = Pj[k-1]; q2 = Pj[k]
                    r = min(r, segment_line_dist(p1, q1, q2))
            for q1 in Pj:
                for k in range(ni):
                    p1 = Pi[k-1]; p2 = Pi[k]
                    r = min(r, segment_line_dist(q1, p1, p2))
            d = r**.5
            G[i].append((j, d))
            G[j].append((i, d))
        d = min(x for x, y in Pi)
        G[i].append((N, d))
        G[N].append((i, d))

        d = W - max(x for x, y in Pi)
        G[i].append((N+1, d))
        G[N+1].append((i, d))

    G[N].append((N+1, W))
    G[N+1].append((N, W))
    que = [(0, N)]
    dist = [10**18]*(N+2)
    dist[N] = 0
    while que:
        cost, v = heappop(que)
        if dist[v] < cost:
            continue
        for w, d in G[v]:
            if cost + d < dist[w]:
                dist[w] = cost + d
                heappush(que, (cost + d, w))
    write("%.16f\n" % dist[N+1])
    return True
while solve():
    ...
