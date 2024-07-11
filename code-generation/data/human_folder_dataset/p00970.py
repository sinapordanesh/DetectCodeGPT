#!/usr/bin/python3

import array
from fractions import Fraction
import functools
import itertools
import math
import os
import sys


def main():
    R, S, P = read_ints()
    A = []
    for _ in range(P):
        i, j = read_ints()
        i -= 1
        j -= 1
        A.append((i, j))

    print(solve(R, S, P, A))


def solve(R, S, P, A):
    q = [0] * (R + S + 1)
    for i, j in A:
        x = S - j if j < S else j - S + 1
        q[R - 1 - i + x] += 1

    of = 0
    for i in range(R + S + 1):
        c = q[i] + of
        if c > 0:
            q[i] = 1
            of = c - 1
    if of > 0:
        return R + S + 1 + of
    while q and q[-1] == 0:
        del q[-1]
    return len(q)


###############################################################################
# AUXILIARY FUNCTIONS

DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def read_int():
    return int(inp())


def read_ints():
    return [int(e) for e in inp().split()]


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


if __name__ == '__main__':
    main()

