from heapq import heappush, heappop
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N, M, S1, S2, T = map(int, readline().split())
    if N == 0:
        return False
    S1 -= 1; S2 -= 1; T -= 1
    G = [[] for i in range(N)]
    Gx = [[] for i in range(N)]
    L = 0
    for i in range(M):
        a, b, w = readline().strip().split()
        a = int(a)-1; b = int(b)-1
        if w == 'x':
            Gx[a].append(b)
            Gx[b].append(a)
            L += 1
        else:
            w = int(w)
            G[a].append((b, w))
            G[b].append((a, w))
    INF = 10**18
    dist = [[INF]*N for i in range(L+1)]
    que = [(0, T, 0)]
    while que:
        cost, v, k = heappop(que)
        if dist[k][v] < cost:
            continue
        dk0 = dist[k]

        for w, d in G[v]:
            if cost + d < dk0[w]:
                dk0[w] = cost + d
                heappush(que, (cost + d, w, k))
        if k+1 <= L:
            dk1 = dist[k+1]
            for w in Gx[v]:
                if cost < dk1[w]:
                    dk1[w] = cost
                    heappush(que, (cost, w, k+1))

    def check(f1, f2, f3):
        return (f2[0] - f1[0]) * (f3[1] - f2[1]) >= (f2[1] - f1[1]) * (f3[0] - f2[0])
    def f(f1, x):
        return f1[0]*x + f1[1]

    que1 = []
    que2 = []
    for a in range(L, -1, -1):
        if dist[a][S1] != INF:
            f1 = (a, dist[a][S1])
            while len(que1) >= 2 and check(que1[-2], que1[-1], f1):
                que1.pop()
            que1.append(f1)

        if dist[a][S2] != INF:
            f2 = (a, dist[a][S2])
            while len(que2) >= 2 and check(que2[-2], que2[-1], f2):
                que2.pop()
            que2.append(f2)
    m1 = len(que1); m2 = len(que2)
    ans = 10**18
    for i in range(m1):
        px0 = 0; px1 = 10**18
        ai, bi = que1[i]
        if i > 0:
            ci, di = que1[i-1]
            px0 = max((bi-di + ci-ai-1) // (ci-ai), 0)
        if i < m1-1:
            ci, di = que1[i+1]
            px1 = (di-bi) // (ai-ci)
        for j in range(m2):
            qx0 = 0; qx1 = 10**18
            aj, bj = que2[j]
            if j > 0:
                cj, dj = que2[j-1]
                qx0 = max((bj-dj + cj-aj-1) // (cj-aj), 0)
            if j < m2-1:
                cj, dj = que2[j+1]
                qx1 = (dj-bj) // (aj-cj)
            x0 = max(px0, qx0); x1 = min(px1, qx1)
            if not x0 <= x1:
                continue
            ans = min(ans, abs((ai - aj)*x0 + (bi - bj)), abs((ai - aj)*x1 + (bi - bj)))
            if ai != aj:
                x = (bj - bi) // (ai - aj)
                if x0 <= x <= x1:
                    ans = min(ans, abs((ai - aj)*x + (bi - bj)))
                if x0 <= x+1 <= x1:
                    ans = min(ans, abs((ai - aj)*(x+1) + (bi - bj)))
    write("%d\n" % ans)
    return True
while solve():
    ...
