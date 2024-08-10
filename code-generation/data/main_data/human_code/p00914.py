def dfs(v, k, s):
    if k == K:
        return 1 if s == S else 0
    res = 0
    for i in range(v + 1, N + 1):
        res += dfs(i, k + 1, s + i)
    return res

while True:
    N, K, S = map(int, input().split())
    if not N:
        break
    print(dfs(0, 0, 0))