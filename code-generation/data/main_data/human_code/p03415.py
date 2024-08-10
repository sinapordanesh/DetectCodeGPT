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


def floor(a, b): return -(-a // b)


def zz(): return list(map(int, sys.stdin.readline().split()))


def z(): return int(sys.stdin.readline())


def S(): return sys.stdin.readline()[:-1]


def C(line): return [sys.stdin.readline() for _ in range(line)]


S = C(3)
print(S[0][0], S[1][1], S[2][2], sep='')
