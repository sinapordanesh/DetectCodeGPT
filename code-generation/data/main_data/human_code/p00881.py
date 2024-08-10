from collections import Counter
import sys
def solve():
    readline = sys.stdin.buffer.readline
    write = sys.stdout.buffer.write
    M, N = map(int, readline().split())
    if M == N == 0:
        return False
    B = [int(readline(), 2) for i in range(N)]
    memo = {}
    def dfs(s, t):
        key = (s, t)
        if key in memo:
            return memo[key]
        c = 0
        for b in B:
            if (b & s) == t:
                c += 1
        if c <= 1:
            memo[key] = 0
            return 0
        res = M
        for i in range(M):
            b = (1 << i)
            if s & b == 0:
                res = min(res, max(dfs(s|b, t), dfs(s|b, t|b))+1)
        memo[key] = res
        return res
    write(b"%d\n" % dfs(0, 0))
    return True
while solve():
    ...
