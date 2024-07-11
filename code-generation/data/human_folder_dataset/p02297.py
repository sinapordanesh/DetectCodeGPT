from sys import stdin
readline = stdin.readline


def dot(a, b):
    return a.real * b.real + a.imag * b.imag


def cross(a, b):
    return a.real * b.imag - a.imag * b.real


def triangle(a, b, c):
    v1, v2 = b - a, c - a
    s = abs(v1) ** 2 * abs(v2) ** 2 - dot(v1, v2) ** 2
    return s ** 0.5 * 0.5


def polygon(p):
    return 0.5 * sum(cross(p[i - 1], p[i]) for i in range(len(p)))


n = int(readline())
p = [map(int, readline().split()) for _ in range(n)]
p = [x + y * 1j for x, y in p]
print('{:.1f}'.format(polygon(p)))