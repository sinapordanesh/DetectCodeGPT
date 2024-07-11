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

def pow(N):
    ret = 1
    for i in range(n):
        ret *= N
        ret %= MOD
    return ret

C = 0
for i in range(k - 1, 0, -1):
    num = fact(k) / fact(i) / fact(k - i) * pow(i)
    if (i - k) % 2 == 1:
        num *= -1
    C += num
print (pow(k) + C) % MOD
