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
    N = int(input())
    a = list(map(int, input().split()))

    avg = sum(a) / N
    min_abs = 10**9
    for i in range(N):
        min_abs = min(min_abs, abs(a[i] - avg))
    for i in range(N):
        if abs(a[i] - avg) == min_abs:
            print(i)
            exit()


if __name__ == '__main__':
    main()
