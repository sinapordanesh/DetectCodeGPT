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
T = getList()
A = getList()

"""
山の高さの列が何通りあるか　dp? 組み合わせ?
dpなら漸化式を考える

5
1 3 3 3 3 高橋くんは左 → 右
3 3 2 2 2 青木くんは右 → 左
最大値のみをレコード

最大値が更新された時のみ高さがわかる
1 3 ? ? ?
? 3 ? ? 2

1 3 ? ? 2
3番目は3以下かつ2以下
4番目は3以下かつ2以下

5
1 1 1 2 2
3 2 1 1 1

1 ? ? 2 ?
3 2 ? ? 1 矛盾
"""

c_t = [-1] * N
c_t[0] = T[0]
for i in range(1, N):
    if T[i] > T[i - 1]:
        c_t[i] = T[i]

c_a = [-1] * N
c_a[N - 1] = A[N - 1]
for i in range(N - 2, -1, -1):
    if A[i] > A[i + 1]:
        c_a[i] = A[i]

c_det = [-1] * N
for i in range(N):
    if c_t[i] >= 0 and c_a[i] >= 0:
        if c_t[i] != c_a[i]:
            print(0)
            exit()
        else:
            c_det[i] = c_t[i]
    elif c_t[i] >= 0:
        c_det[i] = c_t[i]
    elif c_a[i] >= 0:
        c_det[i] = c_a[i]

for i in range(N):
    if c_det[i] > min(T[i], A[i]):
        print(0)
        exit()

ans = 1
for i in range(N):
    if c_det[i] == -1:
        ans *= min(T[i], A[i])
        ans %= mod
print(ans)