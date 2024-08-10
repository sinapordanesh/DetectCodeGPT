from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write

D = [
    (1, 5, 2, 3, 0, 4), # 'U'
    (3, 1, 0, 5, 4, 2), # 'R'
    (4, 0, 2, 3, 5, 1), # 'D'
    (2, 1, 5, 0, 4, 3), # 'L'
]
p_dice = (0, 0, 0, 1, 1, 2, 2, 3)*3

def rotate_dice(L, k):
    return (L[e] for e in D[k])

def enumerate_dice(L0):
    *L, = L0[:]
    for k in p_dice:
        yield L
        L[:] = (L[e] for e in D[k])

def dice_graph():
    L0 = [0, 1, 2, 3, 4, 5]
    DA = list(map(tuple, enumerate_dice(L0)))
    DA.sort()
    DM = {tuple(e): i for i, e in enumerate(DA)}
    G = [list(DM[tuple(rotate_dice(ds, i))] for i in range(4)) for ds in DA]
    return DA, G
DA, DG = dice_graph()

def solve():
    W, D = map(int, readline().split())
    if W == D == 0:
        return False
    clr = "wrgbcmy#"
    MP = [list(map(clr.find, readline().strip())) for i in range(D)]
    vs = list(map(clr.find, readline().strip()))
    ps = [-1]*7
    for i, v in enumerate(vs):
        ps[v] = i
    CX = [0]*8; CY = [0]*8
    for i in range(D):
        s = MP[i]
        for j in range(W):
            k = s[j]
            if k >= 1:
                CX[k] = j; CY[k] = i
                if k == 7:
                    s[j] = 0
    dd = ((0, -1), (1, 0), (0, 1), (-1, 0))
    L = (1, 5, 3, 6, 2, 4)
    sx = CX[7]; sy = CY[7]
    que = deque([(0, sx, sy, 0)])
    dist = [[[{} for i in range(W)] for j in range(D)] for k in range(7)]
    dist[0][sy][sx][0] = 0
    C = [4]*6
    ans = -1
    while que and ans == -1:
        i, x, y, d = que.popleft()
        if C[i] == 0:
            continue
        d0 = dist[i]
        d1 = dist[i+1]
        c = d0[y][x][d]
        for k in range(4):
            dx, dy = dd[k]
            nx = x + dx; ny = y + dy
            if not 0 <= nx < W or not 0 <= ny < D or MP[ny][nx] == -1:
                continue
            nd = DG[d][k]
            if MP[ny][nx] != 0:
                l = L[DA[nd][0]]
                if l != MP[ny][nx] or ps[l] != i:
                    continue
                if nd not in d1[ny][nx]:
                    d1[ny][nx][nd] = c+1
                    C[i] -= 1
                    if i+1 < 6:
                        que.append((i+1, nx, ny, nd))
                    else:
                        ans = c+1
            else:
                if nd not in d0[ny][nx]:
                    d0[ny][nx][nd] = c+1
                    que.append((i, nx, ny, nd))
    if ans != -1:
        write("%d\n" % ans)
    else:
        write("unreachable\n")
    return True
while solve():
    ...
