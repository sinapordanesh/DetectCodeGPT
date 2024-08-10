import sys
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    N, L = map(int, readline().split())
    if N == 0:
        return False
    ma = 0
    P = [list(map(int, readline().split())) for i in range(N)]
    ma = max(u for s, t, u in P)
    K = 86400
    EPS = 1e-8
    def check(x, M = 2):
        rest = L
        R = [0]*M
        for i in range(M):
            prv = 0
            for s, t, u in P:
                rest = min(rest + (s - prv) * x, L)
                rest = min(rest + (t - s) * (x - u), L)
                prv = t
                if rest < 0:
                    return 0
            rest = min(rest + (K - prv) * x, L)
            R[i] = rest
        return R[-2] - EPS < R[-1]
    left = 0; right = ma
    while left + EPS < right:
        mid = (left + right) / 2
        if check(mid):
            right = mid
        else:
            left = mid
    write("%.016f\n" % right)
    return True
while solve():
    ...
