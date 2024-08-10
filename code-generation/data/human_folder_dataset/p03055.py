from sys import setrecursionlimit


def dfs(v):
    def dfs_rec(v):
        for nv in g[v]:
            if d[nv] >= 0:
                continue
            d[nv] = d[v] + 1
            dfs_rec(nv)

    d = [-1] * N
    d[v] = 0
    dfs_rec(v)
    return d


def get_diameter():
    d = dfs(0)
    far = max((d[i], i) for i in range(N))[1]
    return max(dfs(far))


setrecursionlimit(400_000)
N, *ab = map(int, open(0).read().split())
g = [[] for _ in range(N)]
for a, b in zip(*[iter(ab)] * 2):
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

print("Second") if get_diameter() % 3 == 1 else print("First")
