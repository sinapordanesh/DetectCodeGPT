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

N = INT()
s = input()

def is_ok(x, idx):
	if s[idx] == "o":
		if x[idx] == "S" and x[idx-1] == x[idx+1]:
			return True
		elif x[idx] == "W" and x[idx-1] != x[idx+1]:
			return True
		else:
			return False
	elif s[idx] == "x":
		if x[idx] == "S" and x[idx-1] != x[idx+1]:
			return True
		elif x[idx] == "W" and x[idx-1] == x[idx+1]:
			return True
		else:
			return False

start = list(product(["S", "W"], repeat=2))

for i in range(4):
	ws = []
	ws.extend(start[i])
	for j in range(1, N-1):
		if ws[j] == "S":
			if s[j] == "o":
				ws.append(ws[j-1])
			else:
				if ws[j-1] == "S":
					ws.append("W")
				else:
					ws.append("S")
		elif ws[j] == "W":
			if s[j] == "x":
				ws.append(ws[j-1])
			else:
				if ws[j-1] == "S":
					ws.append("W")
				else:
					ws.append("S")
	if is_ok(ws, -1) and is_ok(ws, 0):
		print(*ws, sep="")
		break

else:
	print(-1)

