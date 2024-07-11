from collections import deque
import sys
def main():
    readline = sys.stdin.readline
    write = sys.stdout.write
    def root(x):
        if x == p[x]:
            return x
        p[x] = y = root(p[x])
        return y
    def unite(x, y):
        px = root(x)
        py = root(y)
        if px < py:
            p[py] = px
        else:
            p[px] = py

    N = int(readline())
    *C, = map(int, readline().split())
    M = int(readline())
    *p, = range(N)
    G = [[] for i in range(N)]
    G0 = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, readline().split()); a -= 1; b -= 1
        G[a].append(b)
        G[b].append(a)
        ca = C[a]; cb = C[b]
        if ca < cb:
            G0[a].append(b)
        elif cb < ca:
            G0[b].append(a)
    for v in range(N):
        ws = G[v]
        if not ws:
            continue
        ws.sort(key = C.__getitem__)
        c = C[v]
        prv = ws[0]; pw = C[prv]
        if C[prv] == c:
            unite(v, prv)
        for w in ws[1:]:
            cw = C[w]
            if pw == cw:
                unite(prv, w)
            else:
                G0[prv].append(w)
            if cw == c:
                unite(v, w)
            prv = w; pw = cw

    G1 = [[] for i in range(N)]
    deg = [0]*N
    for v in range(N):
        pv = root(v)
        for w in G0[v]:
            pw = root(w)
            if pv != pw:
                G1[pv].append(pw)
                deg[pw] += 1

    que = deque()
    D = [0]*N
    for i in range(N):
        if root(i) != i:
            continue
        if deg[i] == 0:
            que.append(i)
            D[i] = 1
    while que:
        v = que.popleft()
        d = D[v]
        for w in G1[v]:
            deg[w] -= 1
            if deg[w] == 0:
                que.append(w)
            D[w] = max(D[w], d+1)
    for i in range(N):
        if root(i) == i:
            continue
        D[i] = D[root(i)]
    write("%d\n" % sum(D))
main()
