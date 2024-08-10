mod = 10**9+7
import sys
import math
from collections import Counter, defaultdict, deque
import copy

# from itertools import product, permutations, combinations, combinations_with_replacement
# from itertools import accumulate
# from operator import itemgetter
# from bisect import bisect_bound_list,bisect
# from heapq import heappop,heappush
# from math import ceil,floor
# from copy import deepcopy
# from heapq import heappop,heappush,heapify
# import heapq


# def combinations(n, r):
# 	return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

# def gcd(a, b):
# 	if b == 0:
# 		return a
# 	else:
# 		return gcd(b, a%b)
 
# def lcm(a, b):
# 	return a // gcd(a, b) * b

# l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
# c = Counter(l)

# d = defaultdict(int)

sys.setrecursionlimit(10 ** 6)

int1 = lambda x: int(x) - 1

# リストの要素を改行を挟んで表示する
p2D = lambda x: print(*x, sep="\n")
# 入力を整数に変換して受け取る
def II(): return int(sys.stdin.readline())

def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())

# 入力全てを整数に変換したものの配列を受け取る
# def LI(): return list(map(int, sys.stdin.readline().split()))
# 入力全てを整数に変換して1引いたものの配列を受け取る
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LI(): return list(map(lambda x:int(x), sys.stdin.readline().split()))
def HI(): return list(map(lambda x:int(x)*(-1), sys.stdin.readline().split()))

# import numpy as np
# R, C = MI()
# S = np.array([LI() for _ in range(R)])
# ans = 0
# for i in range(2**R):
#     r = np.array([[i >> r & 1 for r in range(R)]])
#     X = np.sum(S.T ^ r, axis=1)
#     ans = max(ans, np.sum(np.maximum(X, R-X)))
# print(ans)


N,x = MI()
A = LI()
cnt = 0
for i in range(len(A)):
    if i > 0:
        if A[i-1] + A[i] > x:
            cnt += A[i-1] + A[i] - x
            A[i] = A[i] - (A[i-1] + A[i] - x)
    else:
        if A[i] > x:
            cnt += A[i] - x
            A[i] = x
print(cnt)












