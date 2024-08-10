import sys
def gcd(m, n):
    while n:
        m, n = n, m % n
    return m
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    f = lambda h, m, s: 3600*h + 60*m + s
    H, h, m, s = map(int, readline().split())
    if H == 0:
        return False
    d0 = f(h, m, s)
    M = f(H, 0, 0)
    res = []
    for h0 in range(H):
        for m0 in range(60):
            p = 3600*h0 + 60*m0 + 60*H*m0; q = 119*H-1
            for d in [-3600*H, 0, 3600*H]:
                p1 = p + d; q1 = q
                g = gcd(p1, q); p1 //= g; q1 //= g
                if 0 <= p1 < 60*q1:
                    if H*(60*m0*q1 + p1) != q1*(3600*h0 + 60*m0) + p1:
                        res.append((f(h0, m0, 0) + p1/q1, h0, m0, p1, q1))
    res.sort(key = lambda x: (x[0] - d0) % M)
    _, h, m, p, q = res[0]
    write("%d %d %d %d\n" % (h, m, p, q))
    return True
while solve():
    ...
