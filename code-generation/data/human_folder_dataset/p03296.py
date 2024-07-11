import sys, math
from functools import lru_cache
from collections import defaultdict
from decimal import Decimal
sys.setrecursionlimit(10**9)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]

def main():
    N = ii()
    a = list(mi())

    for i in range(N-1):
        if a[i] == a[i+1]:
            a[i+1] = -1
    print(a.count(-1))

if __name__ == '__main__':
    main()
