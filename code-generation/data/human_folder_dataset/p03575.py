# Union Find
# xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


# xとyの属する集合の併合
def unite(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False
    else:
        # x < y にする
        if par[x] > par[y]:
            x, y = y, x
        par[x] += par[y]
        par[y] = x
        return True


# 根の個数を返す
def group_count():
    return sum(x < 0 for x in par)


n, m = map(int, input().split())
l = []
for _ in range(m):
    l.append(tuple(map(int, input().split())))

ans = 0
for j in range(m):
    par = [-1] * n
    for i, ab in enumerate(l):
        if i != j:
            unite(ab[0] - 1, ab[1] - 1)
    if group_count() == 2:
        ans += 1

print(ans)