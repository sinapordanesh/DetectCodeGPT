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

N, K = MAP()
xy = [LIST() for _ in range(N)]
ans = INF

xy.sort()
for l in range(N-K+1):  #長方形の最も左の点
	for r in range(l+K, N+1):  #長方形の最も右の点
		y = sorted(xy[l:r], key = lambda x: x[1]) #lからrの中でyのとりうる値をソート
		for i in range(r-l-K+1):
			sq = (xy[r-1][0] - xy[l][0])*(y[i+K-1][1] - y[i][1])
			ans = min(ans, sq)
print(ans)