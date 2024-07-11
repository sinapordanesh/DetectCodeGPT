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

N, A = MAP()
x = LIST()

X = max(max(x), A)

y = [0]*len(x)
for i in range(len(x)):
	y[i] = x[i]-A

dp = [[0]*(2*N*X+1) for _ in range(N+1)]  #dp[j][t] = y1...yj から0枚以上選んで合計がt-N*Xにするような選び方

for j in range(N+1):
	for t in range(-N*X, N*X+1):
		if j == 0 and t == 0:
			dp[j][t] = 1
		elif j >= 1 and (t-y[j-1] < -N*X or t-y[j-1] > N*X):
			dp[j][t] = dp[j-1][t]
		elif j >= 1 and -N*X <= t-y[j-1] <= N*X:
			dp[j][t] = dp[j-1][t] + dp[j-1][t-y[j-1]]
		else:
			dp[j][t] = 0

print(dp[N][0]-1)

