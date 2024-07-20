from sys import stdin
from operator import attrgetter
readline = stdin.readline


def norm(a):
    return a.real * a.real + a.imag * a.imag


def closest_pair(p):
    if len(p) <= 1:
        return float('inf')
    m = len(p) // 2
    d = min(closest_pair(p[:m]), closest_pair(p[m:]))
    p = [pi for pi in p if p[m].imag - d < pi.imag < p[m].imag + d]
    return brute_force(p, d)

def brute_force(p, d=float('inf')):
    p.sort(key=attrgetter('real'))
    for i in range(1, len(p)):
        for j in reversed(range(i)):
            tmp = p[i] - p[j]
            if d < tmp.real:
                break
            tmp = abs(tmp)
            if d > tmp:
                d = tmp
    return d


def main():
    n = int(readline())
    p = [map(float, readline().split()) for _ in range(n)]
    p = [x + y * 1j for x, y in p]

    p.sort(key=attrgetter('imag'))
    print('{:.6f}'.format(closest_pair(p)))
main()