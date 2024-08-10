from collections import deque
import sys
def main():
    readline = sys.stdin.readline
    write = sys.stdout.write
    W, H = map(int, readline().split())
    MP = [readline() for i in range(H)]
    A = [[-1]*W for i in range(H)]
    B = [[-1]*W for i in range(H)]
    C = [[0]*W for i in range(H)]
    SW0 = 'ABCDEFGHIJ'
    SW1 = 'abcdefghij'
    for i, mp in enumerate(MP):
        Ai = A[i]; Bi = B[i]
        for j, c in enumerate(mp):
            if c == '#':
                continue
            if c in '^' or c in SW0:
                Ai[j] = 1
                if c != '^':
                    Bi[j] = SW0.index(c)+1
            elif c in '_%&' or c in SW1:
                Ai[j] = 0
                if c == '%':
                    sx = j; sy = i
                elif c == '&':
                    gx = j; gy = i
                elif c != '_':
                    Bi[j] = SW1.index(c)+1
            elif c == '|':
                Bi[j] = 0
                Ai[j] = 2
    S = int(readline())
    for k in range(S):
        MP = [readline() for i in range(H)]
        for i, mp in enumerate(MP):
            Ci = C[i]
            for j, c in enumerate(mp):
                if c == '*':
                    Ci[j] |= (2 << k)

    dist = [[{} for i in range(W)] for j in range(H)]
    dist[sy][sx][0] = 0
    dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
    bc = [0]*(2 << S)
    for i in range(1, 2 << S):
        bc[i] = bc[i ^ (i & -i)] ^ 1
    que = deque([(0, sx, sy, 0)])
    while que:
        state, x, y, d = que.popleft()
        if B[y][x] == 0:
            if state^1 not in dist[y][x]:
                dist[y][x][state^1] = d+1
                que.append((state^1, x, y, d+1))
        elif B[y][x] != -1:
            n_state = state ^ (1 << B[y][x]) ^ (state & 1)
            n_state ^= bc[n_state & C[y][x]] ^ A[y][x]
            if n_state not in dist[y][x]:
                dist[y][x][n_state] = d+1
                que.append((n_state, x, y, d+1))
        for dx, dy in dd:
            nx = x + dx; ny = y + dy
            if not 0 <= nx < W or not 0 <= ny < H or A[ny][nx] == -1:
                continue
            if A[ny][nx] == 2:
                if state not in dist[ny][nx]:
                    dist[ny][nx][state] = d+1
                    que.append((state, nx, ny, d+1))
            else:
                np = bc[state & C[ny][nx]] ^ A[ny][nx]
                if state&1 == np and state not in dist[ny][nx]:
                    dist[ny][nx][state] = d+1
                    que.append((state, nx, ny, d+1))
    if dist[gy][gx]:
        write("%d\n" % min(dist[gy][gx].values()))
    else:
        write("-1\n")
main()
