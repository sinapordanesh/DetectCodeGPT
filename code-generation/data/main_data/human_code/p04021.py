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
A = getArray(N)
s = sorted(A)
alta = {}
for i in range(N):
    alta[s[i]] = i
A = [alta[i] for i in A]

"""
N <= 100000
O(NlogN)まで
1つとばし交換をたくさん行う
隣接とばしの最小回数は
N = 4
A = [2, 4, 3, 1]の場合最終形は
A = [1, 2, 3, 4]
バブルソートの交換回数
1, 2, 3の自分より左にある自分より大きいものの数

1, 3, 5...番目にあるものは1, 3, 5...番目にしかいけない
いくつ路線を変える必要があるか
"""

def counter(array):
    n = len(array)
    cnt = 0
    for i in range(n):
        if (array[i] % 2) ^ (i % 2):
            cnt += 1
    return cnt

print(counter(A) // 2)