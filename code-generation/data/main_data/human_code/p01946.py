#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    s, t, d = LI()
    w = LI()
    sumw = sum(w)
    sb = s
    mins = s
    for i in range(d):
        sb += w[i]
        mins = min(mins, sb)
        if sb <= t:
            print(i + 1)
            return
    if sumw >= 0:
        print(-1)
    else:
        ans = ((mins - t) // abs(sumw)) * d
        #print(ans, s, d, t, sumw)
        s += ans // d * sumw
        i = 0
        while 1:
            if s <= t:
                print(ans + i)
                return
            s += w[i%d]
            i += 1
        print(ans+i+1)
    return

#B
def B():
    return

#C
def C():
    return

#D
def D():
    return

#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == '__main__':
    A()

