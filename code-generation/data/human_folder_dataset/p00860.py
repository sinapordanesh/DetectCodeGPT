from heapq import heappush, heappop
from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    W, H, N = map(int, readline().split())
    if W == H == N == 0:
        return False
    MP = [[0]*W for i in range(H)]

    S = [(i-2, i-2) for i in range(3)]
    T = [(i-2, i-2) for i in range(3)]
    for i in range(H):
        s = readline().strip()
        for j, c in enumerate(s):
            if c == '#':
                MP[i][j] = 1
            elif c != ' ':
                idx = "abcABC".find(c)
                if idx < 3:
                    S[idx] = (j, i)
                else:
                    T[idx-3] = (j, i)

    dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
    que = deque([S[0] + (0,)])
    MM = {S[0]: 0, (-1, -1): -2, (0, 0): -1}
    sx, sy = S[0]
    U = [[0]*W for i in range(H)]
    U[sy][sx] = 1
    G = [[0]]
    cur = 1
    while que:
        x, y, v = que.popleft()
        for dx, dy in dd:
            nx = x + dx; ny = y + dy
            if MP[ny][nx] or U[ny][nx]:
                continue
            U[ny][nx] = 1
            MM[nx, ny] = cur
            que.append((nx, ny, cur))
            G.append([cur, v])
            G[v].append(cur)
            cur += 1
    MM[-1, -1] = len(G); G.append([len(G)])
    MM[0, 0] = len(G); G.append([len(G)])
    a0 = MM[S[0]]; b0 = MM[S[1]]; c0 = MM[S[2]]
    a1 = MM[T[0]]; b1 = MM[T[1]]; c1 = MM[T[2]]

    L = cur+2
    def check(s):
        que = deque([s])
        D = [-1]*L
        D[s] = 0
        while que:
            v = que.popleft()
            nd = D[v]+1
            for w in G[v]:
                if D[w] != -1:
                    continue
                D[w] = nd
                que.append(w)
        return D

    D1 = check(a1); D2 = check(b1); D3 = check(c1)
    INF = 10**18

    hcost = max(D1[a0], D2[b0], D3[c0])
    D = {(a0, b0, c0): 0}
    que = [(hcost, 0, a0, b0, c0)]
    g_key = (a1, b1, c1)
    push = heappush; pop = heappop
    while que:
        hcost, cost, a, b, c = pop(que)
        key = (a, b, c)
        if key == g_key:
            break
        if D[key] < cost:
            continue
        nd = cost+1
        for na in G[a]:
            d1 = D1[na]
            for nb in G[b]:
                if na == nb or (nb == a and na == b):
                    continue
                d2 = D2[nb]
                for nc in G[c]:
                    if na == nc or nb == nc or (nc == a and na == c) or (nc == b and nb == c):
                        continue
                    n_key = (na, nb, nc)
                    if nd < D.get(n_key, INF):
                        D[n_key] = nd
                        hcost = max(d1, d2, D3[nc]) + nd
                        push(que, (hcost, nd, na, nb, nc))
    write("%d\n" % D[g_key])
    return True
while solve():
    ...
