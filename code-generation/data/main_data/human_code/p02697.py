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

# 割り当てを一つ求める
# N回Mラウンドを行う 1ラウンドあたりの最大対戦者数はN以下になる

# 対戦者A, B, C, D...にそれぞれ１、２、３、４...を割り当てる
# 試合後、A, B, C, D...の数字は２、３、４、５...になる N + 1になったら１になる
# N, M = 4, 1の時 M1に[1, 2]を割り当てると
#   A B C D
# 1 1 2 3 4 A vs B
# 2 2 3 4 1 D vs A
# 3 3 4 1 2 C vs D
# 4 4 1 2 3 B vs C なのでok
# Nラウンドでちょうど一周するので、M = 1の時は何を入れてもok

# N, M = 5, 2の時
#   A B C D E
# 1 1 2 3 4 5
# 2 2 3 4 5 1
# 3 3 4 5 1 2
# 4 4 5 1 2 3
# 5 5 1 2 3 4

# M1には何を指定してもいい？
# 少なくともM1とM2が同じパターン(i, i+1等)はダメ
# 全てのMについて違うパターンで数字を割り当てられるか
# = 任意のMi(ai, bi), Mj(aj, bj)について abs(bi - ai) != abs(bj - aj)
N, M = getNM()
A = []
B = []
if N % 2 != 0:
    for i in range(M):
        A.append(i + 1)
        B.append(N - i)
else:
    for i in range(M):
        A.append(i + 1)
        if i <= ((N // 4) - 1):
            B.append(N - i)
        else:
            B.append(N - i - 1) # 一つずらす
for i in range(M):
    print(A[i], B[i])


# コーナーケースあり
# 前と後ろから取っていったのではダメなケース？
# ちょうどrotateしたところ
# N, M = 6, 2
# m1に[1, 6], m2に[3, 4]を指定するとダブル
#   A B C D E F
# 1 1 2 3 4 5 6
# 2 2 3 4 5 [6 1] E, F
# 3 3 4 5 6 1 2
# 4 4 5 6 1 2 3
# 5 5 6 1 2 [3 4] E, F
# 6 6 1 2 3 4 5

# rotateしてもダブらないように
# m1に[1, 6], m2に[2, 3]を指定すると
#   A B C D E F
# 1 1 2 3 4 5 6
# 2 2 3 4 5 [6 1] E vs F
# 3 3 4 5 6 1 2
# 4 4 5 6 1 2 3
# 5 5 6 1 2 3 4
# 6 6 1 2 3 4 5

# 偶奇で分かれる？
# 奇数の場合は大丈夫
# m1 間はN - 2(奇数), 0
# m2 間はN - 4(奇数), 2

# 偶数の場合はダメ
# うまくズラして
# m1 間はN - 2(偶数), 0
# m2 間はN - 4(偶数), 2

# m1 間はN - 2, 0
# m2 間はN - 4, 2
# m3 間はN - 6, 4
# ...
# mm-2 間は6, N - 6
# mm-1 間は4, N - 4
# mm 間は2, N - 2
# 関係があるのは1個目とN個目, 2個目とN-1個目...
# 小さい方から半分については１個ずらす