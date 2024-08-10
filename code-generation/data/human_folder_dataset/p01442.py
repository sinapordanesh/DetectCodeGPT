from heapq import heappush, heappop
import sys
readline = sys.stdin.readline
write = sys.stdout.write

dd = ((-1, 0), (0, -1), (1, 0), (0, 1))

def solve():
    H, W, N = map(int, readline().split())
    if H == 0:
        return False
    S = readline().strip()
    C = [[0]*W for i in range(H)]
    sx = sy = gx = gy = 0
    for i in range(H):
        s = readline().strip()
        for j, c in enumerate(s):
            if c in '#.':
                C[i][j] = (c == '#')
            elif c == 'S':
                sx = j; sy = i
            else:
                gx = j; gy = i
    S0 = [1]*(N+1)
    cur = 1
    for i in range(N):
        if S[i] == 'L':
            cur = (cur - 1) % 4
        else:
            cur = (cur + 1) % 4
        S0[i+1] = cur
    d = [N+1]*4
    D = [None]*(N+1)
    for i in range(N, -1, -1):
        d[S0[i]] = i
        D[i] = d[:]

    T = [[N+1]*W for i in range(H)]
    T[sy][sx] = 0
    que = [(0, sx, sy)]
    while que:
        cost, x, y = heappop(que)
        if T[y][x] < cost:
            continue
        d = D[cost]
        for k in range(4):
            dx, dy = dd[k]; n_cost = d[k]
            nx = x + dx; ny = y + dy
            if not 0 <= nx < W or not 0 <= ny < H or C[ny][nx]:
                continue
            if n_cost < T[ny][nx]:
                T[ny][nx] = n_cost
                heappush(que, (n_cost, nx, ny))
    print("Yes" if T[gy][gx] < N+1 else "No")
    return True
while solve():
    ...
