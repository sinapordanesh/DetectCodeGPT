import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a, b, c, d = map(int, input().split())

if a == c or b == d:
    print(0)
    sys.exit(0)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

x = abs(a - c)
y = abs(b - d)

_gcd = gcd(x, y)
x2 = x // _gcd
y2 = y // _gcd

import math

print((x2 + y2 - 1) * _gcd)
