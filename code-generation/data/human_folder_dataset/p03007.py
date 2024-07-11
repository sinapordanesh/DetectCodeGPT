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
#import math
# from itertools import product, accumulate, combinations, product
import bisect
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
    N, *A = mapread()
    A.sort()
    i = bisect.bisect_right(A, -EPS)
    cache = []
    if i <= N-1:
        if i < 1:
            i = 1
        ans = A[i-1]
        for k in range(i, N-1):
            cache.append((ans, A[k]))
            ans -= A[k]
        cache.append((A[N-1], ans))
        ans = A[N-1] - ans
        for k in range(0, i-1):
            cache.append((ans, A[k]))
            ans -= A[k]
        print(ans)
        for x, y in cache:
            print(f'{x} {y}')
    elif i > N-1:
        ans = A[-1]
        for i in range(N-1):
            cache.append((ans, A[i]))
            ans -= A[i]
        print(ans)
        for x, y in cache:
            print(f'{x} {y}')


if __name__ == "__main__":
    #print(math.gcd(0, 10))
    run()
