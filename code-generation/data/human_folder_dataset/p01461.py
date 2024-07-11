from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N = int(readline())
    A = [0]*N
    B = [0]*N
    for i in range(N-1):
        a, b = map(int, readline().split())
        if not a <= b:
            a, b = b, a
        A[i] = a-1
        B[i] = b-1
    que = deque([0])
    vs = []
    dist = [0]*N
    while que:
        v = que.popleft()
        vs.append(v)
        d = dist[v]
        if A[v] != N-1:
            w = A[v]
            que.append(w)
            dist[w] = d+1
        if B[v] != N-1:
            w = B[v]
            que.append(w)
            dist[w] = d+1
    sz = [0]*N
    dp = [[0, 0] for i in range(N)]
    vs.reverse()
    for v in vs:
        a = A[v]; b = B[v]
        if a == N-1:
            dp[v][0] = 2
            dp[v][1] = dist[v] + 2
            sz[v] = 2
        elif b == N-1:
            dp[v][0] = dp[a][0] + sz[a] + 1
            dp[v][1] = dp[a][1] + 1
            sz[v] = sz[a] + 1
        else:
            dp[v][0] = dp[a][0] + dp[b][0] + sz[a] + sz[b]
            dp[v][1] = min(dp[a][0] + dp[b][1] + sz[a], dp[a][1] + dp[b][0] + sz[b], dp[a][1] + dp[b][1])
            sz[v] = sz[a] + sz[b]
    write("%d\n" % dp[0][1])
solve()
