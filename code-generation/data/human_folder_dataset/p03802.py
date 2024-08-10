import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()

def SCC(E):
    n = len(E)
    rev = [[] for _ in range(n)]
    for v in range(n):
        for nv in E[v]:
            rev[nv].append(v)

    used = [0] * n
    order = []
    for v in range(n):
        if used[v]:
            continue
        stack = [~v, v]
        while stack:
            v = stack.pop()
            if v >= 0:
                if used[v]:
                    continue
                used[v] = 1
                for nv in E[v]:
                    if not used[nv]:
                        stack.append(~nv)
                        stack.append(nv)
            else:
                if used[~v] == 2:
                    continue
                used[~v] = 2
                order.append(~v)

    cnt = 0
    color = [-1] * n
    for v in order[::-1]:
        if color[v] != -1:
            continue
        color[v] = cnt
        queue = [v]
        for v in queue:
            for nv in rev[v]:
                if color[nv] == -1:
                    color[nv] = cnt
                    queue.append(nv)
        cnt += 1
    return color

from bisect import bisect_left, bisect_right
def resolve():
    n = int(input())
    ZI = []
    for i in range(n):
        x, y = map(int, input().split())
        ZI.append((x, i)), ZI.append((y, i))
    ZI.sort()

    pair = [[] for _ in range(n)]
    for i, p in enumerate(ZI):
        pair[p[1]].append(i)
    Z = [p[0] for p in ZI]
    n *= 2
    n2 = n * 2

    def check(d):
        N = 1 << (n2 - 1).bit_length()
        E = [[] for _ in range(N * 2)]
        for i in range(N - 1, 0, -1):
            E[i].append(i << 1)
            E[i].append(i << 1 | 1)

        for u, v in pair:
            E[u + N].append(v + n + N)
            E[u + n + N].append(v + N)
            E[v + N].append(u + n + N)
            E[v + n + N].append(u + N)

        for i, z in enumerate(Z):
            L = bisect_right(Z, z - d)
            R = bisect_left(Z, z + d)
            for l, r in [(L + n, i + n), (i + 1 + n, R + n)]:
                l += N
                r += N
                while l < r:
                    if l & 1:
                        E[i + N].append(l)
                        l += 1
                    if r & 1:
                        r -= 1
                        E[i + N].append(r)

                    l >>= 1
                    r >>= 1

        res = SCC(E)
        return all(res[i + N] != res[i + n + N] for i in range(n))

    l = 0
    r = max(Z)
    while r - l > 1:
        m = (l + r) // 2
        if check(m):
            l = m
        else:
            r = m
    print(l)
resolve()