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
    S, T = input(), input()
    dic = defaultdict(lambda : [])
    for i, s in enumerate(S):
        dic[s].append(i)

    k = -1
    ans = 1
    for t in T:
        if t in dic.keys():
            i = bisect.bisect_right(dic[t], k)
            if i >= len(dic[t]):
                k = dic[t][0]
                ans += 1
            else:
                k = dic[t][i]

        else:
            print(-1)
            return

    print((ans-1) * len(S) + k +1)


if __name__ == "__main__":
    #print(math.gcd(0, 10))
    run()
