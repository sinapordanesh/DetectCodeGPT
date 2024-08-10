from collections import defaultdict
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def cross3(p0, p1, p2):
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p1[1] - p0[1]) * (p2[0] - p0[0])

def solve():
    N = int(readline())
    mp = defaultdict(list)
    for i in range(N):
        x, y = map(int, readline().split())
        mp[x].append(y)
    *S, = mp.items()
    S.sort()
    def calc(S, k):
        P = []; Q = []
        r = 0; R = [0]
        for x, ys in S:
            ys.sort(reverse=k)
            for y in ys:
                p = (x, y)
                while len(P) >= 2 and cross3(P[-2], P[-1], p) <= 0:
                    r += abs(cross3(P[-2], P[-1], p))
                    P.pop()
                P.append(p)
                while len(Q) >= 2 and cross3(Q[-2], Q[-1], p) >= 0:
                    r += abs(cross3(Q[-2], Q[-1], p))
                    Q.pop()
                Q.append(p)
            R.append(r)
        return R
    R0 = calc(S, 0)
    S.reverse()
    R1 = calc(S, 1)

    L = len(S)
    ans = 10**20
    for i in range(L+1):
        ans = min(ans, R0[i] + R1[-1-i])
    write("%d\n" % ((ans+1) // 2))
solve()
