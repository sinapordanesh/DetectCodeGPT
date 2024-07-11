import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def dfs(v, c):
        for u in edge[v]:
            if color[u] is None:
                color[u] = c
                dfs(u, c ^ 1)
            else:
                if color[u] != c:
                    print(-1)
                    exit()

    n = int(input())
    S = [list(input()) for _ in range(n)]
    edge = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if S[i][j] == "1":
                edge[i].append(j)
                edge[j].append(i)

    color = [None] * n
    dfs(0, 0)
    for i in range(n):
        for j in range(n):
            if i == j:
                S[i][j] = 0
            else:
                S[i][j] = f_inf if S[i][j] == "0" else 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                S[i][j] = min(S[i][j], S[i][k] + S[k][j])

    res = 0
    for s in S:
        res = max(res, max(s))
    print(res + 1)


if __name__ == '__main__':
    resolve()
