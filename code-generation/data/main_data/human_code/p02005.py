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
def S(): return list(sys.stdin.readline())[:-1]
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

def solve():
    n = I()
    d = defaultdict(lambda : [])
    for i in range(n):
        a,b = input().split()
        b = int(b)
        d[a].append(b)
    for i in d.keys():
        d[i].sort()
    m = I()
    s = 0
    for i in range(m):
        o = input()
        if not d[o]:
            print("No")
            return
        j = bisect.bisect_right(d[o],s)
        if j == len(d[o]):
            print("No")
            return
        s = d[o][j]
    print("Yes")
    return

#Solve
if __name__ == "__main__":
    solve()

