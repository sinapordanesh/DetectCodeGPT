import sys

sys.setrecursionlimit(10 ** 7)


def dfs(v, parent, odd):
    hi = INF
    lo = -INF
    if fixed[v] != INF:
        if odd_even[v] != odd:
            print('No')
            exit()
        hi = lo = fixed[v]
    for u in links[v]:
        if u == parent:
            continue
        chi, clo = dfs(u, v, odd ^ 1)
        if hi < clo or chi < lo:
            print('No')
            exit()
        hi = min(hi, chi)
        lo = max(lo, clo)
    upper[v] = hi
    lower[v] = lo
    return hi + 1, lo - 1


def fill(v, parent, pp):
    if pp + 1 > upper[v]:
        assert pp - 1 >= lower[v]
        vp = fixed[v] = pp - 1
    else:
        vp = fixed[v] = pp + 1
    for u in links[v]:
        if u == parent:
            continue
        fill(u, v, vp)


inp = list(map(int, sys.stdin.buffer.read().split()))
n = inp[0]
links = [set() for _ in range(n)]
for a, b in zip(inp[1:2 * n - 1:2], inp[2:2 * n - 1:2]):
    a -= 1
    b -= 1
    links[a].add(b)
    links[b].add(a)
INF = 10 ** 9
k = inp[2 * n - 1]
fixed = [INF] * n
odd_even = {}
fixed_v = 0
for v, p in zip(inp[2 * n::2], inp[2 * n + 1::2]):
    v -= 1
    fixed[v] = p
    odd_even[v] = p % 2
    fixed_v = v

lower = [-INF] * n
upper = [INF] * n
dfs(fixed_v, -1, odd_even[fixed_v])
fill(fixed_v, -1, fixed[fixed_v] + 1)
print('Yes')
print('\n'.join(map(str, fixed)))
