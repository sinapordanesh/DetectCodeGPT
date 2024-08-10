from sys import stdin
readline = stdin.readline

def main():
    x1, y1, x2, y2 = map(int, readline().split())
    p1, p2 = x1 + y1 * 1j, x2 + y2 * 1j
    q = int(readline())
    for i in range(q):
        xi, yi = map(int, readline().split())
        pi = xi + yi * 1j
        cross = p1 + (p2 - p1) * projecter(p2 - p1, pi - p1)
        cross = cross * 2 - pi
        print('{:.10f} {:.10f}'.format(cross.real, cross.imag))


def projecter(a, b):
    return dot(a, b) / dot(a, a)


def dot(a, b):
    return a.real * b.real + a.imag * b.imag
main()