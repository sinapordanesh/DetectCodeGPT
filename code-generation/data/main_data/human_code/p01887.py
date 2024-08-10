from collections import defaultdict
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    W, H, K = map(int, readline().split())
    N = int(readline())
    mp = defaultdict(lambda:defaultdict(int))
    for i in range(N):
        x, y = map(int, readline().split())
        if y % 2 == 1:
            continue
        if x % 2 == 1:
            mp[y][x//2] |= 1
            if x < W:
                mp[y][x//2+1] |= 4
        else:
            mp[y][x//2] |= 2
    if K < W//2:
        write("-1\n")
        return
    K -= W//2+1
    r = 0
    for y, mp_xs in mp.items():
        *S, = mp_xs.items()
        S.sort()
        a = 0; b = 10**9
        prv = -1
        for x, bs in S:
            if x - prv > 1:
                a = b = min(a, b)
            v0 = ((bs & 1) > 0); v1 = ((bs & 2) > 0); v2 = ((bs & 4) > 0)
            a, b = min(a + v0, b + min(v0+v2, 2*v1)), min(a, b + v2)
            prv = x
        if prv < W // 2:
            c = min(a, b)
        else:
            c = a
        r += c
    ans = max((W//2+1)*(H//2) + max(r - K, 0) - K, 0)
    write("%d\n" % ans)
solve()
