'''
自宅用PCでの解答
'''
import math
#import numpy as np
import itertools
import queue
import bisect
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)
mod = 10**9+7
# mod = 998244353
dir = [(-1,0),(0,-1),(1,0),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"
INF = 1<<32-1
# INF = 10**18

def main():
    n = int(ipt())
    wrds = []
    hq = []
    usd = set()
    for i in range(n):
        s,c = input().split()
        c = int(c)
        wrds.append((s,c))
        hpq.heappush(hq,(c,s,1))

    while hq:
        hc,hs,hp = hpq.heappop(hq)
        usd.add((hs,hp))
        ls = len(hs)
        if hs == hs[::-1]:
            print(hc)
            exit()
        for si,ci in wrds:
            lsi = len(si)
            if lsi > ls:
                if hp == 1:
                    wt = si[::-1]
#                    print(wt)
                    if hs == wt[:ls:] and not (wt[ls::],-1) in usd:
                        hpq.heappush(hq,(hc+ci,wt[ls::],-1))
                else:
                    if hs == si[:ls:] and not (si[ls::],1) in usd:
                        hpq.heappush(hq,(hc+ci,si[ls::],1))
            else:
                if hp == 1:
                    wt = si[::-1]
                    if wt == hs[:lsi:] and not (hs[lsi::],1) in usd:
                        hpq.heappush(hq,(hc+ci,hs[lsi::],1))
                else:
                    if si == hs[:lsi:] and not (hs[lsi::],-1) in usd:
                        hpq.heappush(hq,(hc+ci,hs[lsi::],-1))
#        print(hq)

    print(-1)


    return None

if __name__ == '__main__':
    main()
