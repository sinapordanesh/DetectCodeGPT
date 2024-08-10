from collections import deque
from heapq import heappush, heappop, heapify
import sys
readline = sys.stdin.readline
write = sys.stdout.write

dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
Z = [-1]*(50*50)

def calc(H, W, G, x0, y0, bx, by, S):
    S[:] = Z[:H*W]
    k = y0*W + x0
    que = deque([k])
    S[k] = 0
    for i in [0, 1]:
        for j in [0, 1]:
            S[(by+i)*W + (bx+j)] = -2
    while que:
        v = que.popleft()
        cost = S[v]
        for w in G[v]:
            if S[w] == -1:
                S[w] = cost+1
                que.append(w)
    return S

def solve():
    H, W = map(int, readline().split())
    if H == W == 0:
        return False
    M = [[0]*W for i in range(H)]
    AS = []; BS = []
    for i in range(H):
        s = readline().strip()
        Mi = M[i]
        for j, c in enumerate(s):
            if c == '*':
                Mi[j] = -1
            elif c == 'X':
                Mi[j] = 1
                AS.append((j, i))
            elif c == '.':
                BS.append((j, i))
    G = [[] for i in range(H*W)]
    for y in range(H):
        for x in range(W):
            k = y*W + x
            if M[y][x] == -1:
                continue
            for dx, dy in dd:
                nx = x + dx; ny = y + dy
                if not 0 <= nx < W or not 0 <= ny < H or M[ny][nx] == -1:
                    continue
                G[k].append(ny*W + nx)

    sx, sy = min(AS)
    if sx == sy == 0:
        write("0\n")
        return True

    (x0, y0), (x1, y1) = BS

    ee = [
        ((-1, 0), (-1, 1)),
        ((0, -1), (1, -1)),
        ((2, 0), (2, 1)),
        ((0, 2), (1, 2)),
    ]
    INF = 10**9
    D = [[[INF]*4 for i in range(W)] for j in range(H)]

    d1 = [0]*(H*W)
    d2 = [0]*(H*W)
    calc(H, W, G, x0, y0, sx, sy, d1)
    calc(H, W, G, x1, y1, sx, sy, d2)

    que0 = []
    for i in range(4):
        (dx1, dy1), (dx2, dy2) = ee[i]
        x1 = sx+dx1; y1 = sy+dy1
        x2 = sx+dx2; y2 = sy+dy2
        if not 0 <= x1 <= x2 < W or not 0 <= y1 <= y2 < H:
            continue
        k1 = y1*W + x1; k2 = y2*W + x2
        if d1[k1] == -1 or d2[k2] == -1:
            continue
        d = min(d1[k1] + d2[k2], d1[k2] + d2[k1])
        que0.append((d, sx, sy, i))
        D[sy][sx][i] = d
    heapify(que0)

    while que0:
        cost0, x0, y0, t0 = heappop(que0)
        if D[y0][x0][t0] < cost0:
            continue
        if x0 == y0 == 0:
            break
        (dx1, dy1), (dx2, dy2) = ee[t0]
        x1 = x0 + dx1; y1 = y0 + dy1
        x2 = x0 + dx2; y2 = y0 + dy2
        calc(H, W, G, x1, y1, x0, y0, d1)
        calc(H, W, G, x2, y2, x0, y0, d2)

        for t1 in range(4):
            (dx3, dy3), (dx4, dy4) = ee[t1]
            x3 = x0 + dx3; y3 = y0 + dy3
            x4 = x0 + dx4; y4 = y0 + dy4
            if not 0 <= x3 <= x4 < W or not 0 <= y3 <= y4 < H:
                continue
            k3 = y3*W + x3; k4 = y4*W + x4
            if d1[k3] == -1 or d2[k4] == -1:
                continue
            d = min(d1[k3] + d2[k4], d1[k4] + d2[k3]) + 1
            dx, dy = dd[t1]
            nx = x0 + dx; ny = y0 + dy
            if cost0 + d < D[ny][nx][t1^2]:
                D[ny][nx][t1^2] = cost0 + d
                heappush(que0, (cost0 + d, nx, ny, t1^2))
    res = min(D[0][0][2], D[0][0][3])
    if res != INF:
        write("%d\n" % res)
    else:
        write("-1\n")
    return True
while solve():
    ...
