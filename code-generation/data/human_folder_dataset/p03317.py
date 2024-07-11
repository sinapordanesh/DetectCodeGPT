#!/usr/bin/env python3
import sys
import math
import decimal
import itertools
from itertools import product
from functools import reduce
def input():
    return sys.stdin.readline()[:-1]
def gcd(*numbers):
    return reduce(math.gcd, numbers)
def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)
def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)
def sort_zip(a:list, b:list):
    z = zip(a, b)
    z = sorted(z)
    a, b = zip(*z)
    a = list(a)
    b = list(b)
    return a, b
def ceil(x):
    return math.ceil(x)
def floor(x):
    return math.floor(x)

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = ceil((N - 1) / (K - 1))
    print(ans)


if __name__ == '__main__':
    main()
