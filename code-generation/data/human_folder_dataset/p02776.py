import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
from bisect import bisect_left, bisect_right
def resolve():
    n, m = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(n)]
    AB.sort()
    AB.append([INF, 0])
    for i in range(n, 0, -1):
        AB[i][1] ^= AB[i - 1][1]
    X = [b for a, b in AB]

    E = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v = map(int, input().split())
        l = bisect_left(AB, [u, 0])
        r = bisect_right(AB, [v, 1])
        E[l].append((r, i + 1))
        E[r].append((l, i + 1))

    ans = []
    used = [False] * (n + 1)
    def dfs(v):
        if used[v]:
            return 0
        used[v] = True
        stack = [(~v, -1, -1), (v, -1, -1)]
        while stack:
            v, p, i = stack.pop()
            if v >= 0:
                for nv, i in E[v]:
                    if used[nv]:
                        continue
                    used[nv] = True
                    stack.append((~nv, v, i))
                    stack.append((nv, v, i))
            else:
                v = ~v
                if p != -1:
                    if X[v]:
                        ans.append(i)
                        X[p] ^= 1
                else:
                    return X[v]

    for v in range(n + 1):
        if dfs(v):
            print(-1)
            return

    print(len(ans))
    if ans:
        print(*sorted(ans))
resolve()