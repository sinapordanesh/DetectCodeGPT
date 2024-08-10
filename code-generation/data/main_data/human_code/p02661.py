def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()
def rand_N(ran1, ran2):
    return random.randint(ran1, ran2)
def rand_List(ran1, ran2, rantime):
    return [random.randint(ran1, ran2) for i in range(rantime)]
def rand_ints_nodup(ran1, ran2, rantime):
  ns = []
  while len(ns) < rantime:
    n = random.randint(ran1, ran2)
    if not n in ns:
      ns.append(n)
  return sorted(ns)

def rand_query(ran1, ran2, rantime):
  r_query = []
  while len(r_query) < rantime:
    n_q = rand_ints_nodup(ran1, ran2, 2)
    if not n_q in r_query:
      r_query.append(n_q)
  return sorted(r_query)

from collections import defaultdict, deque, Counter
from sys import exit
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 998244353

#############
# Main Code #
#############

N = getN()
A = []
B = []
for i in range(N):
    a, b = getNM()
    A.append(a)
    B.append(b)
A.sort()
B.sort()
# 範囲がN個ある
# Xは整数
# 中央値のmin, maxは？
# Nが偶数、奇数の場合
# 奇数の場合 中央値は絶対に整数
# 中央値のmin: Aの中央値、max: Bの中央値
# 偶数の場合
# 中央値のmin: (Ai-1 + Ai) / 2 max: (Bi-1 + Bi) / 2
# いくつある？

# 中央値は最低でも0.5刻み
# 偶数の場合は奇数の2N - 1になる？
# Ai-1とAiを自由にいじることで0.5, 1, 1.5と言う風に中間値を作れそう
if N % 2 == 0:
    opt_a = (A[(N // 2) - 1] + A[N // 2]) / 2
    opt_b = (B[(N // 2) - 1] + B[N // 2]) / 2
    # opt_b - opt_aを0.5で割って +1
    print(int((opt_b - opt_a) * 2 + 1))
else:
    opt_a = A[N // 2]
    opt_b = B[N // 2]
    # 中央値は絶対に整数
    print(opt_b - opt_a + 1)