#!/usr/bin/env python

import sys
import math
import itertools as it
from collections import deque

sys.setrecursionlimit(10000000)

MOD = 10 ** 9 + 7
n, k = map(int, raw_input().split())

def fact(N):
    if N <= 1:
        return 1
    return fact(N - 1) * N

print (fact(n + k - 1) / fact(k - 1) / fact(n)) % MOD
