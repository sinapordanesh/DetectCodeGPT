import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
from functools import reduce, lru_cache
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7 
#mod = 998244353
from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10

N, T = MAP()
A = LIST()

buy = [0]*N
sell = [0]*N
buy_memo = [0]*N
sell_memo = [0]*N

tmp_buy = INF
tmp_buy_memo = -1
for i in range(N):
	if A[i] <= tmp_buy:
		tmp_buy = A[i]
		tmp_buy_memo = i
	buy[i] = tmp_buy
	buy_memo[i] = tmp_buy_memo

tmp_sell = 0
tmp_sell_memo = -1
for i in range(N-1, -1, -1):
	if tmp_sell <= A[i]:
		tmp_sell = A[i]
		tmp_sell_memo = i
	sell[i] = tmp_sell
	sell_memo[i] = tmp_sell_memo

diff = [sell[i]-buy[i] for i in range(N)]
max_diff = max(diff)

buy_possible = [0]*N
sell_possible = [0]*N

for i in range(N):
	if diff[i] == max_diff:
		buy_possible[buy_memo[i]] = 1
		sell_possible[sell_memo[i]] = 1

print(min(sum(buy_possible), sum(sell_possible)))
 