#!/usr/bin/python3

import array
from fractions import Fraction
import functools
import itertools
import math
import os
import sys


def main():
    N = read_int()
    A = inp()
    for _ in range(N):
        print('-' if solve(inp(), A) < 0 else '+')


def solve(A, B):
    i = 0
    j = 0
    N = len(A)
    M = len(B)
    while i < N and j < M:
        c = A[i]
        d = B[i]
        if '0' <= c <= '9':
            if '0' <= d <= '9':
                ii = i + 1
                while ii < N and '0' <= A[ii] <= '9':
                    ii += 1
                jj = j + 1
                while jj < M and '0' <= B[jj] <= '9':
                    jj += 1
                a = int(A[i : ii])
                b = int(B[j : jj])
                if a != b:
                    return a - b
                i = ii
                j = jj
            else:
                return -1
        else:
            if '0' <= d <= '9':
                return 1
            if c != d:
                return ord(c) - ord(d)
            i += 1
            j += 1

    if i < N:
        return 1
    if j < M:
        return -1
    return 0


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

