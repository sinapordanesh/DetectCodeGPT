N, W, D = map(int, input().split())
def calc(x0, y0, dx, dy):
    s = min(W - x0 if dx >= 0 else x0, D - y0 if dy >= 0 else y0)
    x = x0 + dx*s; y = y0 + dy*s
    assert x in [0, W] or y in [0, D], (x, y)
    if y == 0:
        return x
    if x == W:
        return W+y
    if y == D:
        return 2*W+D-x
    return 2*W+2*D-y

S = []
for i in range(N):
    x, y, f = input().split(); x = int(x); y = int(y)
    if f == 'N':
        t1 = calc(x, y, 1, 1)
        t2 = calc(x, y, -1, 1)
    elif f == 'E':
        t1 = calc(x, y, 1, -1)
        t2 = calc(x, y, 1, 1)
    elif f == 'S':
        t1 = calc(x, y, -1, -1)
        t2 = calc(x, y, 1, -1)
    else:
        t1 = calc(x, y, -1, 1)
        t2 = calc(x, y, -1, -1)
    if t1 >= t2:
        t1 -= 2*(W+D)
    S.append((t1, t2))
S.sort(key=lambda x: x[1])
ans = N
INF = 10**9
for i in range(N):
    r = 0
    cur = -INF
    base = 0
    for j in range(N):
        a, b = S[(i+j) % N]
        if (i+j) % N == 0:
            base += 2*(W+D)
        if a + base <= cur:
            continue
        cur = b + base
        r += 1
    ans = min(r, ans)
print(ans)
