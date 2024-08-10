import sys, math
from functools import lru_cache
from collections import defaultdict, Counter
import bisect
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
    a, b = i2(3)
    c = a+b
    if c.count(1) == 3 or c.count(2) == 3 or c.count(3) == 3 or c.count(4) == 3:
        print('NO')
    else:
        print('YES')




if __name__ == '__main__':
    main()
