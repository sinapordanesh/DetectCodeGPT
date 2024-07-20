from sys import stdin
readline = stdin.readline


def cross(a, b):
    return a.real * b.imag - a.imag * b.real


def dot(a, b):
    return a.real * b.real + a.imag * b.imag


def diff(p, i):
    return p[(i + 1) % len(p)] - p[i]

# http://www.prefield.com/algorithm/geometry/convex_diameter.html
def convex_diameter(p):
    js = ks = 0
    for i in range(1, len(p)):
        if p[i].imag > p[js].imag:
            js = i
        if p[i].imag < p[ks].imag:
            ks = i

    maxd = abs(p[js] - p[ks])
    j, k = js, ks
    while True:
        if cross(diff(p, j), diff(p, k)) >= 0:
            k = (k + 1) % len(p)
        else:
            j = (j + 1) % len(p)
        if maxd < abs(p[j] - p[k]):
            maxd = abs(p[j] - p[k])
        if j == js and k == ks:
            break
    return maxd


n = int(readline())
p = [map(float, readline().split()) for _ in range(n)]
p = [x + y * 1j for x, y in p]
print('{:.6f}'.format(convex_diameter(p)))