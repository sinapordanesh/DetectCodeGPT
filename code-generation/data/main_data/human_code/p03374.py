import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
from functools import reduce
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

N, C = MAP()
xv = [LIST() for _ in range(N)]

#左回り用
energy_left_1 = [0]
energy_left_2 = [0]
tmp_v = 0
for x, v in xv:
	tmp_v += v
	energy_left_1.append(tmp_v-x)
	energy_left_2.append(tmp_v-2*x)

#右周り用
energy_right_1 = [0]
energy_right_2 = [0]
tmp_v = 0 
for x, v in xv[::-1]:
	y = C-x
	tmp_v += v
	energy_right_1.append(tmp_v-y)
	energy_right_2.append(tmp_v-2*y)

energy_left_1_acc = list(accumulate(energy_left_1, max))
energy_left_2_acc = list(accumulate(energy_left_2, max))
energy_right_1_acc = list(accumulate(energy_right_1, max))
energy_right_2_acc = list(accumulate(energy_right_2, max))

ans = -INF
for i in range(N+1):
	ans = max(ans, energy_left_1_acc[i]+energy_right_2_acc[N-i])
	ans = max(ans, energy_left_2_acc[i]+energy_right_1_acc[N-i])
print(ans)