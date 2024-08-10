import sys, math
from functools import lru_cache
import datetime
sys.setrecursionlimit(500000)
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
    p = list(mi())
    cnt = 0
    for i in range(N):
        if p[i] == i+1:
            if i == N-1:
                p[i-1], p[i] = p[i], p[i-1]
            else:
                p[i], p[i+1] = p[i+1], p[i]
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()