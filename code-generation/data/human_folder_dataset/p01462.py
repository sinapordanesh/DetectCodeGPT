from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N, M, P = map(int, readline().split())
    G = [[] for i in range(N)]
    for i in range(M):
        u, v = map(int, readline().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    N1 = 1 << N
    bc = [0]*N1
    for i in range(1, N1):
        bc[i] = bc[i ^ (i & -i)] + 1
    ec = [0]*N1
    for state in range(1, N1):
        c = 0
        for v in range(N):
            if (state & (1 << v)) == 0:
                continue
            for w in G[v]:
                if (state & (1 << w)) == 0:
                    continue
                c += 1
        ec[state] = c >> 1
    N0 = 1 << (N-1)
    dp = [0]*N1
    dp[1] = 1
    for s0 in range(1, N0):
        state0 = (s0 << 1) | 1
        state1 = (state0-1) & state0
        v = 0
        while state1:
            if state1 & 1:
                k = ec[state0] - ec[state1] - ec[state0 ^ state1]
                v += dp[state1] * (P/100)**k
            state1 = (state1 - 1) & state0
        dp[state0] = 1 - v
    write("%.16f\n" % dp[N1-1])
solve()
