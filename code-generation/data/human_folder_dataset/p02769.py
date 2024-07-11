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

# 逆元事前処理ver
# nが小さい場合に
lim = 10 ** 6 + 1
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, lim + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    # 累計
    factinv.append((factinv[-1] * inv[-1]) % mod)

def cmb(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod

N, K = getNM()

# 部屋がn個
# 重複組み合わせ？

# つまり数え上げ
# 人数が0人の部屋がいくつあるか
# 0 ~ N - 1人
# 0人の部屋が0個の場合
# kが偶数ならいける kが1の場合はダメ
# kの回数は何か関係あるか

# k >= 2の時0人の部屋0人ができる
# 0人の部屋1人ができるのは？　k >= 1の時

if K >= 2:
    ans = 1 # 0人の部屋0人
else:
    ans = 0

for k in range(1, min(K + 1, N)):
    # 0の場所を決める *
    # 球があるN - kの部屋の仕切りN - k - 1の仕切り方について考える
    # ただし各部屋１個以上なければならないので自由に動かせる球はk個
    # kHN-k-1
    ans += cmb(N, k) * cmb(N - 1, N - k - 1)
    ans %= mod
print(ans % mod)