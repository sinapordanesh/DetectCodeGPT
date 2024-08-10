#!/usr/bin/python3

import os
import sys


def main():
    N = read_int()
    V = read_ints()
    print(solve(N, V))


def solve(N, V):
    V.sort()
    pos = {}
    for i, a in enumerate(V):
        pos[a] = i
    best = 2
    done = [[False] * N for _ in range(N)]
    for i in range(N):
        a = V[i]
        for j in range(i + 1, N):
            if done[i][j]:
                continue
            b = V[j]
            d = b - a
            c = 2
            done[i][j] = True
            k = j
            v = b + d
            while v in pos:
                done[k][pos[v]] = True
                k = pos[v]
                c += 1
                v += d
            best = max(best, c)
    return best


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

