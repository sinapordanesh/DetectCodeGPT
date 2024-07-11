from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
from pprint import pprint
from copy import deepcopy
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce
from pprint import pprint


sys.setrecursionlimit(2147483647)
INF = 10 ** 20
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007


n, k = LI()

fac = [1] * (n + 1)
inv = [1] * (n + 1)
for j in range(1, n + 1):
    fac[j] = fac[j-1] * j % mod


inv[n] = pow(fac[n], mod-2, mod)
for j in range(n-1, -1, -1):
    inv[j] = inv[j+1] * (j+1) % mod

def comb(n, r):
    if r > n or n < 0 or r < 0:
        return 0
    return fac[n] * inv[n - r] * inv[r] % mod




A = LI()
dp = [[0] * (n + 1) for _ in range(k + 1)]
dp[0][0] = 1
for i in range(k):
    for j in range(n + 1):
        for l in range(min(n - j, A[i]) + 1):
            dp[i + 1][j + l] = (dp[i + 1][j + l] + dp[i][j] * comb(n - j, l) % mod
                                * comb(n - l, A[i] - l)) % mod

print(dp[k][n])