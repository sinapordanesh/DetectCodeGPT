import sys, math
from functools import lru_cache
import heapq
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

def solve(s, e, x, y):
    cnt = 0
    if s:
        x *= -1
        cnt += 1
    if e:
        y *= -1
        cnt += 1

    if y-x>=0:
        cnt += y-x
        return cnt
    else:
        return math.inf


def main():
    x, y = mi()
    ss = [True, True, False, False]
    es = [True, False, True, False]
    m = math.inf

    for i in range(4):
        m = min(m, solve(ss[i], es[i], x, y))

    print(m)



if __name__ == '__main__':
    main()
