m = int(input())
P = [list(map(int, input().split())) for i in range(m)]
s = set()
for i in range(m):
    xi, yi = P[i]
    for j in range(i+1, m):
        xj, yj = P[j]
        u = xj - xi; v = yj - yi
        for x, y in s:
            if x * v == y * u:
                break
        else:
            s.add((u, v))
memo = {}
def dfs(state, dx, dy):
    if (state, dx, dy) in memo:
        return memo[state, dx, dy]
    pstate = state
    update = 1
    cnt = -1
    while update:
        update = 0; cnt += 1
        for i in range(m):
            if (state >> i) & 1:
                continue
            xi, yi = P[i]
            for j in range(i+1, m):
                if (state >> j) & 1:
                    continue
                xj, yj = P[j]
                u = xj - xi; v = yj - yi
                if dx * v == dy * u:
                    update = 1
                    state |= (1 << i) | (1 << j)
                    break
            if update: break
    if cnt <= 1:
        res = 0
    else:
        res = cnt*(cnt-1)//2 + max(dfs(state, *e) for e in s)
    memo[pstate, dx, dy] = res
    return res
print(max(dfs(0, *e) for e in s))