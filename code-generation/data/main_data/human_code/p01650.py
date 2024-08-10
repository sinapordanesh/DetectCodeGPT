import sys
readline = sys.stdin.readline
write = sys.stdout.write
from string import ascii_lowercase, ascii_uppercase
from collections import deque

dd = ((1, 0), (0, 1))

def solve():
    H, W = map(int, readline().split())
    if H == W == 0:
        return False
    C = [readline().strip() for i in range(H)]
    INF = 10**9

    def search(x0, y0, c):
        que = deque([(x0, y0)])
        used = [[0]*W for i in range(H)]
        used[y0][x0] = 1
        r = []
        while que:
            x, y = que.popleft()
            if C[y][x] == c:
                r.append((x, y))
            if x+1 < W and C[y][x+1] != '#' and not used[y][x+1]:
                que.append((x+1, y))
                used[y][x+1] = 1
            if y+1 < H and C[y+1][x] != '#' and not used[y+1][x]:
                que.append((x, y+1))
                used[y+1][x] = 1
        return r, used
    D0, U0 = search(0, 0, None)
    if not U0[H-1][W-1]:
        write("-1\n")
        return True

    D = [[None]*W for i in range(H)]
    U = [[None]*W for i in range(H)]
    K = [[-1]*W for i in range(H)]
    for i in range(H):
        for j in range(W):
            d = C[i][j]
            if d == '#':
                continue
            k = ascii_lowercase.find(C[i][j])
            c = ascii_uppercase[k] if k != -1 else None
            D[i][j], U[i][j] = search(j, i, c)
            K[i][j] = k
    dp = [[[[0]*W for i in range(H)] for j in range(W)] for k in range(H)]
    for i0 in range(H-1, -1, -1):
        for j0 in range(W-1, -1, -1):
            if C[i0][j0] == '#':
                continue
            k = K[i0][j0]
            for i1 in range(H-1, i0-1, -1):
                for j1 in range(W-1, j0-1, -1):
                    if not U[i0][j0][i1][j1]:
                        continue
                    r = max(
                        (dp[i0+1][j0][i1][j1] if i0+1 <= i1 and C[i0+1][j0] != '#' else 0),
                        (dp[i0][j0+1][i1][j1] if j0+1 <= j1 and C[i0][j0+1] != '#' else 0),
                    )
                    if k != -1:
                        for x, y in D[i0][j0]:
                            if not i0 <= y <= i1 or not j0 <= x <= j1 or not U[i0][j0][y][x] or not U[y][x][i1][j1]:
                                continue
                            if (x-j0)+(y-i0) == 1:
                                A = 1
                            else:
                                if i0 == y:
                                    A = dp[i0][j0+1][y][x-1] + 1
                                elif j0 == x:
                                    A = dp[i0+1][j0][y-1][x] + 1
                                else:
                                    A = max(
                                        dp[i0+1][j0][y][x-1],
                                        dp[i0][j0+1][y-1][x],
                                        dp[i0+1][j0][y-1][x] if i0+1 <= y-1 else 0,
                                        dp[i0][j0+1][y][x-1] if j0+1 <= x-1 else 0,
                                    ) + 1
                            r = max(r, A + dp[y][x][i1][j1])
                    dp[i0][j0][i1][j1] = r
    write("%d\n" % dp[0][0][H-1][W-1])
    return True
while solve():
    ...
