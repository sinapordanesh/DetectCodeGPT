import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop, heapify
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

N = INT()
A = LIST()

LR = [[A[-1], A[-1]]]
for i, b in enumerate(A[::-1][1:], 1):
	if N-i+1 < 30:
		LR.append([-(-LR[-1][0]//2)+b, min(LR[-1][1]+b, pow(2, N-i+1))])
	else:
		LR.append([-(-LR[-1][0]//2)+b, LR[-1][1]+b])


LR = LR[::-1]
if LR[0][0] <= 1 <= LR[0][1]:
	pass
else:
	print(-1)
	exit()

ans = 1
tmp = 1
for i, (L, R) in enumerate(LR[1:], 1):
	tmp = min(2*tmp-A[i], R-A[i])
	ans += tmp+A[i]

print(ans)