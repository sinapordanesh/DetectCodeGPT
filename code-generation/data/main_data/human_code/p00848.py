#!usr/bin/env python3
import sys
import math
import string
import collections
import fractions
import random
from operator import itemgetter
import itertools
from collections import deque
import copy
import heapq
import bisect

MOD = 10 ** 9 + 7
INF = float('inf')
input = lambda: sys.stdin.readline().strip()

sys.setrecursionlimit(10 ** 8)


def judge_prime_num(n):
    if n % 2 == 0 and n != 2:
        return False
    else:
        for num in range(3, int(math.sqrt(n) + 2)):
            if n % num == 0:
                return False
        return True


prime_list = []
for i in range(2, 1121):
    if judge_prime_num(i):
        prime_list.append(i)

dp = [[[0] * 1122 for _ in range(16)] for _ in range(190)]
dp[0][0][0] = 1
for i in range(len(prime_list)):
    for j in range(15):
        for k in range(1121):
            if k + prime_list[i] <= 1120:
                dp[i + 1][j + 1][k + prime_list[i]] += dp[i][j][k]
            dp[i + 1][j][k] += dp[i][j][k]
n, k = map(int, input().split())
while not n == k == 0:
    print(dp[len(prime_list)][k][n])
    n, k = map(int, input().split())

