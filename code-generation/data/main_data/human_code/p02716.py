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
mod = 10 ** 9 + 7

#############
# Main Code #
#############

N = getN()
A = getList()

# N // 2個の整数をどの２箇所も連続しないように選ぶ
# 和の最大値を求めよ

# 通りの数は？　まあまあ多い
# 偶数の場合
# 始点がA[1]なら１通りに定まる
# 始点がA[0]なら?
# 次に3個先を取ると1通りに定まる
# 次に2個先を取り、その次に3個先を取ると1通りに定まる

# dp[i][j]: i回目までに3つ飛ばしをj回使った
# 長さが偶数なら1回まで使える
if N % 2 == 0:
    dp = [[-float('inf')] * 2 for i in range(N)]
    dp[0][0] = A[0]
    dp[1][0] = A[1]
    for i in range(2, N):
        for j in range(1, -1, -1):
            if j == 0:
                dp[i][j] = max(dp[i][j], dp[i - 2][j] + A[i])
            elif j == 1 and i - 3 >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 2][j] + A[i])
            if i - 3 >= 0 and j - 1 >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 3][j - 1] + A[i])
    # 0個飛ばしdp[-2]:奇数個目だけ 0個飛ばしdp[-1]:偶数個目だけ 1個飛ばしdp[-1]
    print(max(dp[-2][0], dp[-1][0], dp[-1][1]))
# 長さが奇数なら2回まで使える
else:
    dp = [[-float('inf')] * 3 for i in range(N)]
    dp[0][0] = A[0]
    dp[1][0] = A[1]
    for i in range(2, N):
        for j in range(2, -1, -1):
            if j == 0:
                dp[i][j] = max(dp[i][j], dp[i - 2][j] + A[i])
            elif j >= 1 and i - 3 >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 2][j] + A[i])
            if i - 3 >= 0 and j - 1 >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 3][j - 1] + A[i])
    opt_1 = [A[i] for i in range(N) if i % 2 == 0]
    opt_2 = [A[i] for i in range(N) if i % 2 == 1]
    # 2個飛ばしならdp[-1]のが該当
    # 1個飛ばしならdp[-1], dp[-2]のが該当
    # 0個飛ばしは奇数個目だけ - その中の最小値、偶数個目だけ
    print(max(dp[-1][2], dp[-1][1], dp[-2][1], sum(opt_1) - min(opt_1), sum(opt_2)))