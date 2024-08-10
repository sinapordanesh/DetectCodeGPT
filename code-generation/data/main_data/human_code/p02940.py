'''
研究室PCでの解答
'''
import math
#import numpy as np
import queue
import bisect
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)
mod = 998244353
dir = [(-1,0),(1,0),(0,-1),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"


def main():
    n = int(ipt())
    s = input()
    d = {"R":0,"G":1,"B":2}
    nm = 1
    nc = [0,0,0]
    stt = [0,0,0]
    res = [0,0,0]
    for si in s:
        i = d[si]
        nc[i] += 1
        if nc[i] > nc[i-1] and nc[i] > nc[i-2]:
            stt[i] += 1
        elif nc[i] <= nc[i-1] and nc[i] <= nc[i-2]:
            nm *= res[i]
            res[i] -= 1
        else:
            if stt[i-1] == 0:
                res[i-1] += 1
                nm *= stt[i-2]
                stt[i-2] -= 1
            else:
                res[i-2] += 1
                nm *= stt[i-1]
                stt[i-1] -= 1
        nm %= mod

    for i in range(1,n+1):
        nm *= i
        nm %= mod
    print(nm)

    return None

if __name__ == '__main__':
    main()
