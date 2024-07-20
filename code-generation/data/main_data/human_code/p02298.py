from sys import stdin
readline = stdin.readline


def cross(a, b):
    return a.real * b.imag - a.imag * b.real


def is_convex(p):
    for i in range(len(p)):
        j, k = i - 1, i - 2
        if 0 > cross(p[j] - p[k], p[i] - p[k]):
            return False
    return True

n = int(readline())
p = [map(int, readline().split()) for _ in range(n)]
p = [x + y * 1j for x, y in p]
print(1 if is_convex(p) else 0)