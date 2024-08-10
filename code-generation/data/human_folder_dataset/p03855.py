from collections import Counter


n, k, l = map(int, input().split())

def root(x):
    while p[x] >= 0:
        x = p[x]
    return x

def unite(x, y):
    x, y = root(x), root(y)
    if x == y:
        return
    if x > y:
        x, y = y, x
    p[x] += p[y]
    p[y] = x

def g(x):
    global p
    p = [-1]*n
    for _ in range(x):
        a, b = map(int, input().split())
        unite(a-1, b-1)
    return [root(i) for i in range(n)]

z = [*zip(g(k), g(l))]
count = Counter(z)
print(*[count[t] for t in z])
