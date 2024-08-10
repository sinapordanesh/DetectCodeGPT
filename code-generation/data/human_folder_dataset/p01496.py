from collections import deque
from string import ascii_lowercase, ascii_uppercase, digits
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

ss = digits + ascii_uppercase + ascii_lowercase
L = len(ss)

def rotate_dice(L, k):
    return [L[e] for e in D[k]]
def enumerate_dice(L0):
    L = L0[:]
    for k in p_dice:
        yield L
        L[:] = (L[e] for e in D[k])
def dice_graph(L0 = [0, 1, 2, 3, 4, 5]):
    DA = list(map(tuple, enumerate_dice(L0)))
    DM = {tuple(e): i for i, e in enumerate(DA)}
    G = [list(DM[tuple(rotate_dice(ds, i))] for i in range(4)) for ds in DA]
    return DA, G

def solve():
    H, W = map(int, readline().split())
    S = [readline().strip() for i in range(H)]

    DA, DG = dice_graph()
    dd = ((0, -1), (1, 0), (0, 1), (-1, 0))

    DS = []
    used = [[0]*W for i in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.' or used[i][j]:
                continue
            D = [0]*6
            que = deque([(j, i, 0)])
            used[i][j] = 1
            while que:
                x, y, k = que.popleft()
                v = DA[k][0]
                c = S[y][x]
                if c == '#':
                    D[v] = L
                else:
                    D[v] = ss.index(c)
                for e, (dx, dy) in enumerate(dd):
                    nx = x + dx; ny = y + dy
                    if not 0 <= nx < W or not 0 <= ny < H or S[ny][nx] == '.' or used[ny][nx]:
                        continue
                    used[ny][nx] = 1
                    que.append((nx, ny, DG[k][e]))
            if D.count(L) != 3:
                continue
            for e in enumerate_dice(D):
                if e[3] == e[4] == e[5] == L:
                    if e[0] != e[1] and e[1] != e[2] and e[2] != e[0]:
                        DS.append(e[:3])
                    break
    P = [
        [0, 3, 4],
        [0, 2, 3],
        [0, 1, 2],
        [0, 4, 1],
        [3, 2, 5],
        [2, 1, 5],
        [1, 4, 5],
        [4, 3, 5],
    ]
    DS.sort()
    M = len(DS)
    def dfs(i, used, used_c, state):
        if i == 8:
            return 1
        ps = P[i]
        s = [0]*3
        for j in range(M):
            if used[j]:
                continue
            used[j] = 1
            d = DS[j]
            for b in range(3):
                for k in range(3):
                    p = ps[k]
                    if state[p] == -1:
                        if used_c[d[-b+k]]:
                            break
                    else:
                        if state[p] != d[-b+k]:
                            break
                else:
                    for k in range(3):
                        p = ps[k]
                        if state[p] == -1:
                            used_c[d[-b+k]] = 1
                        s[k], state[p] = state[p], d[-b+k]
                    if dfs(i+1, used, used_c, state):
                        return 1
                    for k in range(3):
                        p = ps[k]
                        state[p] = s[k]
                        if state[p] == -1:
                            used_c[d[-b+k]] = 0
            used[j] = 0
        return 0
    if M >= 8 and dfs(0, [0]*M, [0]*L, [-1]*6):
        write("Yes\n")
    else:
        write("No\n")
solve()
