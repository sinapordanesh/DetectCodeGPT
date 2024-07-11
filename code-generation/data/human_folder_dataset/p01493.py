from collections import deque
import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N = int(readline())
    G = [[] for i in range(N)]
    for i in range(N):
        *vs, = readline()
        for j in range(N):
            if vs[j] == "Y":
                G[i].append(j)
    d = 0
    C = [0, 0]
    used = [0]*N
    for i in range(N):
        d += len(G[i])
        if used[i]:
            continue
        used[i] = 1
        que = deque([i])
        c = 0
        while que:
            v = que.popleft()
            c += 1
            for w in G[v]:
                if used[w]:
                    continue
                used[w] = 1
                que.append(w)
        C[c % 2] += 1
    r0 = (N*(N-1)//2 - d//2) & 1
    memo = {}
    def dfs(i, p, q):
        key = (p, q)
        if key in memo:
            return memo[key]
        if p+q == 2:
            r = (q == 2) ^ r0
            memo[key] = e = r ^ (i & 1)
            return e
        r = 0
        if p > 1 or (p and q):
            if dfs(i+1, p-1, q) == 0:
                r = 1
        if q > 1:
            if dfs(i+1, p+1, q-2) == 0:
                r = 1
        memo[key] = r
        return r
    if dfs(0, C[0], C[1]):
        write("Taro\n")
    else:
        write("Hanako\n")
solve()

