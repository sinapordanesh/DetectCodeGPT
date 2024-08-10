import sys, math, re
from functools import lru_cache
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
    S = input()
    d = {}
    for i in range(N):
        if not S[i] in d:
            d[S[i]] = 1
        d[S[i]] += 1

    ans = 1
    for v in d.values():
        ans *= v
        ans %= MOD

    ans -= 1
    print(ans%MOD)

if __name__ == "__main__":
    main()