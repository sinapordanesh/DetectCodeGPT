import sys
readline = sys.stdin.readline
write = sys.stdout.write
sys.setrecursionlimit(10**5)
def solve():
    N, M = map(int, readline().split())
    G = [[] for i in range(N)]
    for i in range(N-1):
        a, b, c = map(int, readline().split())
        G[a-1].append((b-1, c))
        G[b-1].append((a-1, c))
    *C, = map(int, readline().split())
    def dfs(v, p, s, A):
        m = 0
        for w, d in G[v]:
            if w == p:
                continue
            r = dfs(w, v, s, A) + s*d
            if m < r:
                m, r = r, m
            if r > 0:
                A.append(r)
        return m
    A = []
    for i in range(N):
        r = dfs(i, -1, C[i], A)
        if r > 0:
            A.append(r)
    A.sort(reverse=1)
    write("%d\n" % sum(A[:M]))
solve()
