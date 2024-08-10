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
#from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10

S = input()[::-1]

arr = []
for i, x in enumerate(S):
	if x in digits:
		n = pow(10, i, 13)*int(x)%13
		arr.append(n)
	else:
		arr.append(pow(10, i, 13))

dp = [[0]*13 for _ in range(len(S)+1)]
#dp[i][j] : i桁目までで13で割って余る可能性の数
dp[0][0] = 1

for i, x in enumerate(arr, 1):
	if S[i-1] == "?":
		for k in range(10):
			for j in range(13):
				dp[i][j] += dp[i-1][(j-k*x)%13]
				dp[i][j] %= mod

	else:
		for j in range(13):
			dp[i][j] += dp[i-1][(j-int(x))%13]
			dp[i][j] %= mod


print(dp[-1][5])
