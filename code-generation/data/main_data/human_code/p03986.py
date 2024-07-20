# -*- coding: utf-8 -*-
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect
import copy
import math
from itertools import accumulate
sys.setrecursionlimit(10**6)

# lis_of_lis = [[] for _ in range(N)]


def zz(): return list(map(int, sys.stdin.readline().split()))


def z(): return int(sys.stdin.readline())


def S(): return sys.stdin.readline()[:-1]


def C(line): return [sys.stdin.readline() for _ in range(line)]


X = S()
num_S = [0] * len(X)
t_count = 0
s_count = 0
ans = 0
prev = X[-1]
if (prev == 'S'):
    s_count = 1
else:
    t_count = 1
for x in reversed(X[:-1]):
    if (prev == 'S' and x == 'T'):
        # リセット
        rest = max(s_count - t_count, 0)
        ans += (rest*2)
        t_count = max(t_count - s_count, 0)
        s_count = 0
    if (x == 'S'):
        s_count += 1
    if (x == 'T'):
        t_count += 1
    prev = x
print(ans)


# for i, x in enumerate(X):
#     if(x == 'S'):
#         num_S[i] = 1

# num_S = list(accumulate(num_S))
# print(num_S)
