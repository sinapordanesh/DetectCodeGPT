import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N, Q, A, B, C, D, E, F, G = map(int, readline().split())
    d = 0; rx = 0; ry = 0
    *X, = range(N)
    *Y, = range(N)
    def fc(d, x, y):
        if d == 0:
            return x, y
        if d == 1:
            return y, N-1-x
        if d == 2:
            return N-1-x, N-1-y
        return N-1-y, x
    mp = {}
    for i in range(Q):
        c, *g = readline().strip().split()
        c0, c1 = c
        if c0 == "R":
            if c1 == "L":
                d = (d - 1) % 4
            elif c1 == "R":
                d = (d + 1) % 4
            elif c1 == "H":
                if d & 1:
                    rx ^= 1
                else:
                    ry ^= 1
            else: #c1 == "V":
                if d & 1:
                    ry ^= 1
                else:
                    rx ^= 1
        elif c0 == "S":
            a, b = map(int, g); a -= 1; b -= 1
            if c1 == "R":
                if d & 1:
                    if rx != ((d & 2) > 0):
                        a = N-1-a; b = N-1-b
                    X[a], X[b] = X[b], X[a]
                else:
                    if ry != ((d & 2) > 0):
                        a = N-1-a; b = N-1-b
                    Y[a], Y[b] = Y[b], Y[a]
            else: #c1 == "C":
                if d & 1:
                    if ((d & 2) == 0) != ry:
                        a = N-1-a; b = N-1-b
                    Y[a], Y[b] = Y[b], Y[a]
                else:
                    if ((d & 2) > 0) != rx:
                        a = N-1-a; b = N-1-b
                    X[a], X[b] = X[b], X[a]
        elif c0 == "C": #c == "CP":
            y1, x1, y2, x2 = map(int, g); x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
            x1, y1 = fc(d, x1, y1)
            x2, y2 = fc(d, x2, y2)
            if rx:
                x1 = N-1-x1; x2 = N-1-x2
            if ry:
                y1 = N-1-y1; y2 = N-1-y2
            key1 = (X[x1], Y[y1]); key2 = (X[x2], Y[y2])
            if key1 not in mp:
                xa, ya = key1
                mp[key2] = (ya*A + xa*B + A + B) % C
            else:
                mp[key2] = mp[key1]
        else: #c == "WR":
            y, x, v = map(int, g); x -= 1; y -= 1
            x, y = fc(d, x, y)
            if rx:
                x = N-1-x
            if ry:
                y = N-1-y
            key = (X[x], Y[y])
            mp[key] = v
    MOD = 10**9 + 7
    h = 314159265
    for y in range(D-1, E):
        for x in range(F-1, G):
            x0, y0 = fc(d, x, y)
            if rx:
                x0 = N-1-x0
            if ry:
                y0 = N-1-y0
            x0 = X[x0]; y0 = Y[y0]
            key = (x0, y0)
            if key in mp:
                v = mp[key]
            else:
                v = ((y0+1)*A + (x0+1)*B) % C
            h = (31 * h + v) % MOD
    write("%d\n" % h)
solve()
