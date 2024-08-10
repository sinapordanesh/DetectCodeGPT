from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    N = int(readline())
    if N == 0:
        return False
    sx, sy, tx, ty = map(int, readline().split())
    C = []
    G = [[] for i in range(N+2)]
    L = 0
    for i in range(N):
        xi, yi, ri = map(int, readline().split())
        sc = ((sx - xi)**2 + (sy - yi)**2 <= ri**2)
        tc = ((tx - xi)**2 + (ty - yi)**2 <= ri**2)
        if (sc and tc) or (not sc and not tc):
            continue
        for j in range(L):
            xj, yj, rj = C[j]
            dd = (xi - xj)**2 + (yi - yj)**2
            rr = (ri - rj)**2
            if dd < rr:
                if ri < rj:
                    G[L].append(j)
                elif ri > rj:
                    G[j].append(L)
        if tc:
            G[N].append(L)
        if sc:
            G[N+1].append(L)
        C.append((xi, yi, ri))
        L += 1

    def calc(s):
        que = deque([s])
        used = [0]*(N+2)
        deg = [0]*(N+2)
        used[s] = 1
        while que:
            v = que.popleft()
            for w in G[v]:
                deg[w] += 1
                if used[w]:
                    continue
                used[w] = 1
                que.append(w)
        que = deque([s])
        dist = [0]*(N+2)
        while que:
            v = que.popleft()
            d = dist[v]+1
            for w in G[v]:
                deg[w] -= 1
                dist[w] = max(dist[w], d)
                if deg[w] == 0:
                    que.append(w)
        return dist
    d0 = calc(N); d1 = calc(N+1)
    ans = max(max(d0), max(d1))
    for i in range(L):
        if d0[i] == 0:
            continue
        xi, yi, ri = C[i]
        for j in range(L):
            if d1[j] == 0:
                continue
            xj, yj, rj = C[j]
            if (xi - xj)**2 + (yi - yj)**2 > (ri + rj)**2:
                ans = max(ans, d0[i] + d1[j])
    write("%d\n" % ans)
    return True
while solve():
    ...
