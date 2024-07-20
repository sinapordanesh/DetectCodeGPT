from collections import deque, defaultdict
import sys
readline = sys.stdin.readline
write = sys.stdout.write
dd = ((-1, 0), (0, -1), (1, 0), (0, 1), (0, 0))
def solve():
    W, H = map(int, readline().split())
    if W == H == 0:
        return False
    S = [readline().strip() for i in range(H)]
    px = py = qx = qy = 0
    rs = []
    pp = []
    MP = [[0]*W for i in range(H)]
    for i in range(H):
        for j, c in enumerate(S[i]):
            if c == "Q":
                px = j; py = i
            elif c == "A":
                qx = j; qy = i
            elif c == "E":
                MP[i][j] = 1
                rs.append((j, i))
            elif c == "#":
                MP[i][j] = 2
            if c != "#":
                pp.append((j, i))
    mp = {}
    L = 0
    for ax, ay in pp:
        for bx, by in pp:
            mp[ax, ay, bx, by, 0] = L
            L += 1
            mp[ax, ay, bx, by, 1] = L
            L += 1

    que1 = deque()
    ss = [-1]*L
    cc = [0]*L

    que = deque([(px, py, qx, qy, 0)])
    used = [0]*L
    used[mp[px, py, qx, qy, 0]] = 1
    RG = [[] for i in range(L)]
    deg = [0]*L
    while que:
        ax, ay, bx, by, t = key = que.popleft()
        k0 = mp[key]
        if ax == bx and ay == by:
            que1.append(k0)
            ss[k0] = 1
            continue
        if t == 0 and MP[ay][ax] == 1:
            que1.append(k0)
            ss[k0] = 0
            continue
        if t == 1:
            for dx, dy in dd:
                nx = bx + dx; ny = by + dy
                if not 0 <= nx < W or not 0 <= ny < H or MP[ny][nx] == 2:
                    continue
                k1 = mp[ax, ay, nx, ny, t^1]
                deg[k0] += 1
                RG[k1].append(k0)
                if not used[k1]:
                    used[k1] = 1
                    que.append((ax, ay, nx, ny, t^1))
        else:
            for dx, dy in dd:
                nx = ax + dx; ny = ay + dy
                if not 0 <= nx < W or not 0 <= ny < H or MP[ny][nx] == 2:
                    continue
                k1 = mp[nx, ny, bx, by, t^1]
                deg[k0] += 1
                RG[k1].append(k0)
                if not used[k1]:
                    used[k1] = 1
                    que.append((nx, ny, bx, by, t^1))

    while que1:
        v = que1.popleft()
        s = ss[v]; t = v % 2
        if t == 0:
            for w in RG[v]:
                if ss[w] != -1:
                    continue
                if s == 1:
                    que1.append(w)
                    ss[w] = 1
                else:
                    deg[w] -= 1
                    if deg[w] == 0:
                        que1.append(w)
                        ss[w] = 0
        else:
            for w in RG[v]:
                if ss[w] != -1:
                    continue
                if s == 0:
                    que1.append(w)
                    ss[w] = 0
                else:
                    deg[w] -= 1
                    if deg[w] == 0:
                        que1.append(w)
                        ss[w] = 1
    k0 = mp[px, py, qx, qy, 0]
    if ss[k0] == -1:
        write("Queen can not escape and Army can not catch Queen.\n")
    elif ss[k0] == 0:
        write("Queen can escape.\n")
    else:
        write("Army can catch Queen.\n")
    return True
while solve():
    ...
