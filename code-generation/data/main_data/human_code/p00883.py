from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write

dd0 = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
DD = []
for k in range(6):
    ddk = []
    for y in range(k):
        for x in range(k):
            v = 0
            for dx, dy in dd0:
                nx = x + dx; ny = y + dy
                if not 0 <= nx < k or not 0 <= ny < k:
                    continue
                v |= 1 << (ny*k + nx)
            ddk.append(v)
    DD.append(ddk)
L = (1 << 16)
bc = [0]*L
for v in range(1, L):
    bc[v] = bc[v ^ (v & -v)] + 1

def solve():
    N = int(readline())
    if N == 0:
        return False
    dd = dd0
    dk = DD[N]
    state = 0
    for i in range(N):
        s = readline().strip()
        for j, c in enumerate(s):
            if c == '#':
                state |= 1 << (N*i + j)
            elif c == '@':
                sx = j; sy = i
    U = {(state, sx, sy): 0}
    que = deque([(state, sx, sy)])
    while que:
        state, x, y = key = que.popleft()
        d = U[key]
        if state == 0:
            write("%d\n" % d)
            break
        for dx, dy in dd:
            nx = x + dx; ny = y + dy
            if not 0 <= nx < N or not 0 <= ny < N:
                continue
            b = 1 << (ny*N + nx)
            if state & b:
                continue
            state ^= b
            n_state = 0
            for k in range(N*N):
                v = state & dk[k]
                if state & (1 << k):
                    if v and 2 <= bc[v // (v & -v)] <= 3:
                        n_state |= (1 << k)
                else:
                    if v and bc[v // (v & -v)] == 3:
                        n_state |= (1 << k)
            if n_state & b:
                n_state ^= b
            n_key = (n_state, nx, ny)
            if n_key not in U:
                U[n_key] = d+1
                que.append(n_key)
            state ^= b
    else:
        write("-1\n")
    return True
while solve():
    ...
