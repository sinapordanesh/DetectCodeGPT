from bisect import bisect
import sys
readline = sys.stdin.readline
write = sys.stdout.write

def construct(N, S, base, MOD):
    L = 26
    root = [0, 0, N-1, [None]*L]
    nds = [root]
    for i, s in enumerate(S):
        node = root
        for c in s:
            h, a, b, nt = node
            if nt[c] is None:
                h1 = (h * base + c+1) % MOD
                nt[c] = nd = [h1, i, i, [None]*L]
                nds.append(nd)
            else:
                nd = nt[c]
                nd[1] = min(i, nd[1])
                nd[2] = max(i, nd[2])
            node = nt[c]
    H = {}
    for h, a, b, _ in nds:
        H[h] = (a, b)
    return H

def solve():
    N, Q = map(int, readline().split())

    MOD = 10**18 + 3; base = 41
    ca = ord('a')
    f = lambda x: ord(x) - ca
    A = [list(map(f, readline().strip())) for i in range(N)]
    A.sort()
    ha = construct(N, A, base, MOD)
    B = [(s[::-1], i) for i, s in enumerate(A)]
    B.sort(key = lambda x: x[0])
    C = [0]*N
    for i, (b, j) in enumerate(B):
        C[j] = i
    B = [b for b, j in B]
    hb = construct(N, B, base, MOD)

    N0 = 2**(N-1).bit_length()
    data = [None]*(2*N0)
    for i in range(N):
        data[N0-1+i] = [C[i]]
    for i in range(N, N0):
        data[N0-1+i] = [-1]
    for i in range(N0-2, -1, -1):
        p = data[2*i+1]; q = data[2*i+2]
        pl = len(p); ql = len(q)
        res = [0]*(pl + ql)
        a = b = 0
        while a < pl and b < ql:
            if p[a] < q[b]:
                res[a+b] = p[a]
                a += 1
            else:
                res[a+b] = q[b]
                b += 1
        while a < pl:
            res[a+b] = p[a]
            a += 1
        while b < ql:
            res[a+b] = q[b]
            b += 1
        data[i] = res

    def query(l, r, a, b):
        L = l + N0; R = r + N0
        s = 0
        while L < R:
            if R & 1:
                R -= 1
                s += bisect(data[R-1], b-1) - bisect(data[R-1], a-1)
            if L & 1:
                s += bisect(data[L-1], b-1) - bisect(data[L-1], a-1)
                L += 1
            L >>= 1; R >>= 1
        return s
    for i in range(Q):
        p, s = readline().strip().split()
        h1 = h2 = 0
        for c in map(f, p):
            h1 = (h1 * base + c+1) % MOD
        for c in map(f, s[::-1]):
            h2 = (h2 * base + c+1) % MOD
        if h1 not in ha or h2 not in hb:
            write("0\n")
            continue
        p0, p1 = ha[h1]
        q0, q1 = hb[h2]
        write("%d\n" % query(p0, p1+1, q0, q1+1))
solve()
