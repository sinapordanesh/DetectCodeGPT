import sys
readline = sys.stdin.readline
write = sys.stdout.write

def dot3(O, A, B):
    ox, oy = O; ax, ay = A; bx, by = B
    return (ax - ox) * (bx - ox) + (ay - oy) * (by - oy)
def cross3(O, A, B):
    ox, oy = O; ax, ay = A; bx, by = B
    return (ax - ox) * (by - oy) - (bx - ox) * (ay - oy)
def dist2(A, B):
    ax, ay = A; bx, by = B
    return (ax - bx) ** 2 + (ay - by) ** 2
def is_intersection(P0, P1, Q0, Q1):
    C0 = cross3(P0, P1, Q0)
    C1 = cross3(P0, P1, Q1)
    D0 = cross3(Q0, Q1, P0)
    D1 = cross3(Q0, Q1, P1)
    if C0 == C1 == 0:
        E0 = dot3(P0, P1, Q0)
        E1 = dot3(P0, P1, Q1)
        if not E0 < E1:
            E0, E1 = E1, E0
        return E0 <= dist2(P0, P1) and 0 <= E1
    return C0 * C1 <= 0 and D0 * D1 <= 0

def solve():
    N = int(readline())
    if N == 0:
        return False
    LS = []
    for i in range(N):
        xa, ya, xb, yb = map(int, readline().split())
        LS.append(((xa, ya), (xb, yb)))
    *p, = range(N)
    def root(x):
        if x == p[x]:
            return x
        p[x] = y = root(p[x])
        return y
    def unite(x, y):
        px = root(x); py = root(y)
        if px < py:
            p[py] = px
        else:
            p[px] = py
    for i in range(N):
        p0, p1 = LS[i]
        for j in range(i):
            q0, q1 = LS[j]
            if is_intersection(p0, p1, q0, q1):
                unite(i, j)
    M = 0
    G = []
    lb = [0]*N
    for i in range(N):
        if root(i) == i:
            G.append([LS[i]])
            lb[i] = M
            M += 1
            continue
        e = lb[root(i)]
        G[e].append(LS[i])
    ans = [0]*10
    for g in G:
        if len(g) == 1:
            ans[1] += 1
            continue
        s = {}
        for p0, p1 in g:
            s[p0] = s.get(p0, 0) + 1
            s[p1] = s.get(p1, 0) + 1

        if len(g) == 5:
            d = {}
            for p0, p1 in g:
                v0 = s[p0]; v1 = s[p1]
                key = ((v0, v1) if v0 < v1 else (v1, v0))
                d[key] = d.get(key, 0) + 1
            if (1, 1) in d:
                ans[8] += 1
            else:
                ls = []
                for p0, p1 in g:
                    if s[p0] == 1:
                        ls.append((p0, p1))
                    if s[p1] == 1:
                        ls.append((p1, p0))
                (p0, p1), (q0, q1) = ls
                for e in g:
                    r0, r1 = e
                    if s[r0] != 2 or s[r1] != 2:
                        continue
                    if (is_intersection(p0, p1, r0, r1) and p1 not in e) or (is_intersection(q0, q1, r0, r1) and q1 not in e):
                        ans[6] += 1
                        break
                else:
                    if cross3(p0, p1, q1) < 0:
                        ans[2] += 1
                    else:
                        ans[5] += 1
            continue

        if len(g) == 3:
            if len(s) == 4:
                ans[7] += 1
            else:
                ans[4] += 1
        elif len(g) == 4:
            if len(s) == 4:
                ans[0] += 1
            elif len(s) == 5:
                ans[9] += 1
            else:
                ans[3] += 1
    write(" ".join(map(str, ans)))
    write("\n")
    return True
while solve():
    ...
