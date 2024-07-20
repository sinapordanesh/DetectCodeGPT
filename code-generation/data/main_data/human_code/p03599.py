# coding: utf-8
import sys

# from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
printout = sys.stdout.write
sprint = sys.stdout.flush
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
import math
# from itertools import product, accumulate, combinations, product
#import bisect
# import numpy as np
# from copy import deepcopy
#from collections import deque
# from decimal import Decimal
# from numba import jit

INF = 1 << 50
EPS = 1e-8
mod = 998244353


def intread():
    return int(sysread())
def mapline(t=int):
    return map(t, sysread().split())
def mapread(t=int):
    return map(t, read().split())


def run():
    A, B, C, D, E, F = mapline()
    aa = 100 * A
    bb = 100 * B
    max_con = 0
    ans = (100 * A, 0)
    for x in range(0, F // aa + 1):
        ylim = (F - aa * x) // bb
        for y in range(0, ylim + 1):
            tot = aa * x + bb * y
            if not tot:continue
            slim = E * (x * A + y * B)
            #print(tot, slim)
            for w in range(0, slim // C + 1):
                vlim = (slim - w * C) // D
                for v in range(0, vlim + 1):
                    sug = C * w + D * v
                    #print(sug)
                    if tot + sug <= F:
                        _con = sug / (tot + sug)
                        if max_con < _con:
                            max_con = _con
                            ans = (tot + sug, sug)
    print(f'{ans[0]} {ans[1]}')


if __name__ == "__main__":
    run()
