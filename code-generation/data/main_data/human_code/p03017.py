import sys, math
from functools import lru_cache
from itertools import accumulate
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

N, A, B, C, D = mi()
S = input()
f = (not '##' in S[A-1:C]) and (not '##' in S[B-1:D])
if C > D:
    f = f and ('...' in S[B-2:D+1])

print('Yes' if f else 'No')
