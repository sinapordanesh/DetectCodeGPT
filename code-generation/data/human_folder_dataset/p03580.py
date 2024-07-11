from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce


sys.setrecursionlimit(2147483647)
INF = 10 ** 13
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().rstrip().split()
def S(): return sys.stdin.readline().rstrip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 10 ** 9 + 7


n = I()
s = list(S())
ans = 0
one_cnt = 0
z_cnt = 0
dp = []
flg = 0
for i in range(n):
    if s[i] == "1":
        one_cnt += 1
        z_cnt = 0
        if flg:
            if dp:
                ans += max(dp)
                dp = []
            flg = 0
        if i == n - 1 or s[i + 1] == "0":
            # 手付かず、左端だけ消した、右端だけ残す、全て消した。
            if dp:
                if one_cnt >= 2:
                    ndp = [max(dp), max(dp[0] + pre, dp[1] + pre - 1, dp[2] + 1),
                           max(dp[0], dp[1], dp[2]) + one_cnt - 1,
                           max(dp[0], dp[1], dp[2]) + one_cnt]
                else:
                    ndp = [-INF, -INF, max(dp),
                           max(dp[0] + pre, dp[1] + pre - 1, dp[2] + 1)]
                dp = ndp
            else:
                dp = [0, -INF, -INF, -INF]
            pre = one_cnt
    else:
        z_cnt += 1
        one_cnt = 0
        if z_cnt >= 2:
            flg = 1

if dp:
    ans += max(dp)

print(ans)