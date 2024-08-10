# coding: utf-8
import sys

# from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
printout = sys.stdout.write
sprint = sys.stdout.flush
# from heapq import heappop, heappush
from collections import defaultdict
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
    S = input()
    G = 0
    P = 0
    score = 0
    for s in S:
        if s == 'g':
            if G > P:
                score += 1
                P += 1
            else:
                G += 1
        if s == 'p':
            if G > P:
                P += 1
            else:
                G += 1
                score -= 1

    print(score)

if __name__ == "__main__":
    #print(math.gcd(0, 10))
    run()
