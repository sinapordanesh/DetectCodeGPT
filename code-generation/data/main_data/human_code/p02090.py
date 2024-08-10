#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007


#A
def A():
    n = I()
    a = LI()
    s = sum([i%2 for i in a])
    if s in (0,n):
        print(0)
    else:
        print(n-2+(s%2))
    return

#B
def B():
    n,Q,L,R = LI()
    a = LI()
    a.sort()
    query = LIR(Q)
    l = -1
    r = n
    while r-l > 1:
        m = (l+r)>>1
        am = a[m]
        for q,x,s,t in query:
            if q == 1:
                if am < x:
                    continue
                am += s
                am *= t
            else:
                if am > x:
                    continue
                am -= s
                if am < 0:
                    am = -((-am)//t)
                else:
                    am //= t
        if am < L:
            l = m
        else:
            r = m
    left = r
    l = 0
    r = n
    while r-l > 1:
        m = (l+r)>>1
        am = a[m]
        for q,x,s,t in query:
            if q == 1:
                if am < x:
                    continue
                am += s
                am *= t
            else:
                if am > x:
                    continue
                am -= s
                if am < 0:
                    am = -((-am)//t)
                else:
                    am //= t
        if am <= R:
            l = m
        else:
            r = m
    print(r-left)
    return

#C
def C():
    n,m = LI()
    lis = set()
    f = defaultdict(lambda : 0)
    for i in range(n):
        l,r = LI()
        f[l] += 1
        f[r+0.1] -= 1
        lis.add(l)
        lis.add(r)
        lis.add(r+0.1)
    l = list(lis)
    l.sort()
    k = len(l)
    for i in range(k-1):
        f[l[i+1]] += f[l[i]]
    s = [0,0]
    for i in l:
        j = f[i]
        if s[1] < j:
            s = [i,j]
        elif s[1] == j:
            if s[1]%2:
                s = [i,j]
                
    if s[1]%2:
        print((s[1]>>1)*2*m+round(s[0]))
    else:
        print(s[1]*m-round(s[0]))
    return

#D
def D():
    n = I()

    return

#E
def E():
    n = I()

    return

#F
def F():
    n = I()

    return

#G
def G():
    n = I()

    return

#H
def H():
    n = I()

    return

#I
def I_():
    n = I()

    return

#J
def J():
    n = I()

    return

#Solve
if __name__ == "__main__":
    C()

