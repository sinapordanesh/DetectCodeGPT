l, k = map(int, input().split())
memo = {(l, 0): 1, (l, 1): 0}
def dfs(cur, dark):
    if (cur, dark) in memo:
        return memo[cur, dark]
    res = dfs(cur + 1, dark^1) + (dark^1)
    if dark and cur + k <= l:
            res += dfs(cur + k, dark^1)
    memo[cur, dark] = res
    return res
print(dfs(0, 1))