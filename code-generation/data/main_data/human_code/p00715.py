from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    N = int(readline())
    if N == 0:
        return False
    L = 0
    n_map = {}
    def get(s):
        nonlocal L
        if s in n_map:
            return n_map[s]
        n_map[s] = L
        L += 1
        return L-1

    G = [[] for i in range(2*N)]
    RG = [[] for i in range(2*N)]
    for i in range(N):
        a, b = readline().strip().split("-")
        ka = get(a); kb = get(b)
        G[ka].append(kb)
        RG[kb].append(ka)

    F = [[-1]*L for i in range(L)]
    for v in range(L):
        for w1 in G[v]:
            for w2 in G[v]:
                F[w1][w2] = 1
        for w1 in RG[v]:
            for w2 in RG[v]:
                F[w1][w2] = 1
    for v in range(L):
        for w1 in G[v]:
            for w2 in RG[v]:
                F[w1][w2] = F[w2][w1] = 0

    G0 = [[] for i in range(L)]
    for v in range(L):
        for w in range(L):
            if F[v][w] == 1:
                G0[v].append(w)
                G0[w].append(v)

    PS = []
    que = deque()
    for i in range(L):
        P = [-1]*L
        que.append(i)
        P[i] = 0
        while que:
            v = que.popleft()
            p = P[v]
            for w in G[v]:
                if P[w] != -1:
                    continue
                P[w] = p^1
                que.append(w)
            for w in G0[v]:
                if P[w] != -1:
                    continue
                P[w] = p
                que.append(w)
        PS.append(P)

    write("%d\n" % L)
    M = int(readline())
    for i in range(M):
        a, b = readline().strip().split("-")
        ka = n_map.get(a, -1); kb = n_map.get(b, -1)
        if ka == -1 or kb == -1:
            write("NO\n")
            continue
        write("YES\n" if PS[ka][kb] == 1 else "NO\n")
    return True
while solve():
    ...

