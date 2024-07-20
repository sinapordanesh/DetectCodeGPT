N, W = map(int, input().split())

WVs = [list(map(int, input().split())) for _ in range(N)]

memo = {}
def dp(i, capacity):
    if i == N:
        return 0
    if (i, capacity) in memo:
        return memo[(i, capacity)]
    ret = dp(i+1, capacity)
    w, v = WVs[i]
    if w <= capacity:
        ret2 = dp(i+1, capacity - w) + v
        ret = ret if ret > ret2 else ret2
    memo[(i, capacity)] = ret
    return ret

print(dp(0, W))
