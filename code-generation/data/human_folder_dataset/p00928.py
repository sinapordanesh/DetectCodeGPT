from collections import deque

import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    L = 55
    N, x0, y0, T = map(int, readline().split())
    X = [[0]*L for i in range(L)]
    Y = [[0]*L for i in range(L)]
    Z = [[0]*L for i in range(L)]
    for i in range(N):
        xs, ys, xe, ye = map(int, readline().split())
        if xs == xe:
            if not ys < ye:
                ys, ye = ye, ys
            for j in range(ys, ye):
                X[xs][j] = Z[j][xs] = 1
            Z[ye][xs] = 1
        else:
            if not xs < xe:
                xs, xe = xe, xs
            for j in range(xs, xe):
                Y[ys][j] = Z[ys][j] = 1
            Z[ys][xe] = 1
    DR = "WNES"
    R = [[[None]*4 for i in range(L)] for j in range(L)]
    E = [[[0]*4 for i in range(L)] for j in range(L)]
    U = [[[0]*L for i in range(L)] for j in range(4)]
    U0, U1, U2, U3 = U
    col = 0
    for i in range(L):
        for j in range(L):
            if not Z[i][j]:
                continue
            if Y[i][j-1]:
                E[i][j][0] = 1
            if X[j][i]:
                E[i][j][1] = 1
            if Y[i][j]:
                E[i][j][2] = 1
            if X[j][i-1]:
                E[i][j][3] = 1
            for l in range(4):
                S = [(j, i, l)]
                res = [S]
                for k in range(10):
                    col += 1
                    S1 = []
                    push = S1.append
                    for x, y, e in S:
                        if e != 2 and Y[y][x-1] and U0[y][x-1] != col:
                            U0[y][x-1] = col
                            push((x-1, y, 0))
                        if e != 3 and X[x][y] and U1[y+1][x] != col:
                            U1[y+1][x] = col
                            push((x, y+1, 1))
                        if e != 0 and Y[y][x] and U2[y][x+1] != col:
                            U2[y][x+1] = col
                            push((x+1, y, 2))
                        if e != 1 and X[x][y-1] and U3[y-1][x] != col:
                            U3[y-1][x] = col
                            push((x, y-1, 3))
                    res.append(S1)
                    S = S1
                R[i][j][l] = res
    dd = ((-1, 0), (0, 1), (1, 0), (0, -1))
    S = set()
    d, s = readline().strip().split(); d = int(d); s = DR.index(s)
    for l in range(4):
        if not E[y0][x0][l]:
            continue
        dx, dy = dd[l]
        for x, y, e in R[y0+dy][x0+dx][l][d-1]:
            if e == s:
                for l1 in range(4):
                    if l1 == (e + 2) % 4 or not E[y][x][l1]:
                        continue
                    S.add((x, y, l1))
            elif (e + 2) % 4 != s and E[y][x][s]:
                S.add((x, y, s))

    for i in range(T-1):
        S1 = set()
        d, s = readline().strip().split(); d = int(d); s = DR.index(s)
        for x1, y1, e1 in S:
            if not E[y1][x1][e1]:
                continue
            dx, dy = dd[e1]
            for x, y, e in R[y1+dy][x1+dx][e1][d-1]:
                if e == s:
                    for l1 in range(4):
                        if l1 == (e + 2) % 4 or not E[y][x][l1]:
                            continue
                        S1.add((x, y, l1))
                elif (e + 2) % 4 != s and E[y][x][s]:
                    S1.add((x, y, s))
        S = S1
    P = sorted(set((x, y) for x, y, _ in S))
    for x, y in P:
        write("%d %d\n" % (x, y))
solve()
