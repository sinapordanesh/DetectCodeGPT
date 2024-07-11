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
mod = 10**9+7 #998244353
dir = [(-1,0),(1,0),(0,-1),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"


def main():
    a,b,c,d,e,f,g = map(int,ipt().split())
    ans = (a//2*2+b+d//2*2+e//2*2)
    if a*d*e%2:
        ans += 3
    elif (d*e%2 and a != 0) or (a*d%2 and e != 0) or (a*e%2 and d != 0):
        ans += 1
    print(ans)

    return None

if __name__ == '__main__':
    main()
