# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
#import math
#from itertools import product, accumulate, combinations, product
#import bisect
#import numpy as np
#from copy import deepcopy
#from collections import deque
#from decimal import Decimal
#from numba import jit

INF = 1 << 50
EPS = 1e-8
mod = 10 ** 9 + 7
def intread():
    return int(sysread())
def mapline(t = int):
    return map(t, sysread().split())
def mapread(t = int):
    return map(t, read().split())


def run():
    N, *A = mapread()
    run = False
    ans = 0
    count = 0
    for a in A:
        if run:
            if not a:
                ans += count // 2
                run = False
                count = 0
            else:
                count += a
        else:
            if not a:
                continue
            else:
                run = True
                count += a
    ans += count // 2
    print(ans)

if __name__ == "__main__":
    run()
