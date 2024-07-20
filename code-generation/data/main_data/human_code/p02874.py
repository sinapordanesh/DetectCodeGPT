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
mod = 10**9+7 #998244353
dir = [(-1,0),(0,-1),(1,0),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"
INF = 10**18

def main():
    n = int(ipt())
    base = 10**9
    qs = []
    # Lの最大、Rの最小を求めると同時に、それらが同じセットに入るときのansの最大値を求める
    lma = 0
    li = -1
    ll = 0
    rmi = INF
    ri = INF
    lr = 0
    mal = 0
    for i in range(n):
        l,r = map(int,ipt().split())
        qs.append((l,r))
        d = r-l+1
        f = True
        if l > lma:
            if ll > mal:
                mal = ll
            lma = l
            li = i
            ll = d
            f = False
        elif l == lma and ll > d:
            li = i
            mal = max(mal,ll)
            ll = d
            f = False
        if r < rmi:
            if lr > mal:
                mal = lr
            rmi = r
            ri = i
            lr = d
            f = False
        elif r == rmi and lr > d:
            ri = i
            mal = max(mal,lr)
            lr = d
            f = False
        if f and mal < d:
            mal = d
    ans = mal+max(0,rmi-lma+1)

    # Lの最大値とRの最大値が別のセットに入る場合
    q = []
    for la,ra in qs:
        v = (base-1-max(0,ra-lma+1))*base+max(0,rmi-la+1)
        q.append(v)
    q.sort()
    dp0 = [INF,0]
    dp1 = [0,INF]
    f = False
    for i in q:
        l = base-1-i//base
        r = i%base
        if f:
            dp1[1] = min(dp1[1],r)
            if dp0[0]+r > sum(dp1):
                dp1[0] = dp0[0]
                dp1[1] = r
        f = True
        dp0[0] = min(dp0[0],l)

    # 上二つのうち最大を取る
    print(max(ans,sum(dp1)))
    
    return None

if __name__ == '__main__':
    main()
