#!/usr/bin/python3

import array
from fractions import Fraction
import functools
import itertools
import math
import os
import sys


def main():
    while True:
        H, W = read_ints()
        if (H, W) == (0, 0):
            break
        R = [inp() for _ in range(H)]
        S = inp()
        print(solve(H, W, R, S))


def solve(H, W, R, S):
    pos_map = {}
    for y in range(H):
        for x in range(W):
            c = R[y][x]
            if c != '_':
                pos_map[c] = (x, y)

    ans = 0
    cx = 0
    cy = 0
    for c in S:
        x, y = pos_map[c]
        ans += abs(x - cx) + abs(y - cy) + 1
        cx, cy = x, y

    return ans


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

