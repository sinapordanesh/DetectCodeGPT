from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write
sys.setrecursionlimit(10**5)
def solve():
    N, M, K = map(int, readline().split())
    G = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, readline().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    *D, = map(len, G)
    *I, = range(N)
    I.sort(key = D.__getitem__, reverse = 1)
    INF = 10**9
    def dfs(i, state, c):
        if i == N:
            return c

        v = I[i]
        res = INF

        e1 = []
        for w in G[v]:
            if state[w]:
                continue
            e1.append(w)

        if c + len(e1) <= K:
            for w in e1:
                state[w] = 1
            k = i+1
            while k < N and state[I[k]]:
                k += 1
            res = min(res, dfs(k, state, c+len(e1)))
            for w in e1:
                state[w] = 0

        if len(e1) > 1 and c+1 <= K:
            state[v] = 1
            k = i
            while k < N and state[I[k]]:
                k += 1
            res = min(res, dfs(k, state, c+1))
            state[v] = 0
        return res

    res = dfs(0, [0]*N, 0)
    if res < INF:
        write("%d\n" % res)
    else:
        write("Impossible\n")
solve()
