#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
import sys
import math
import bisect
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

def solve():
    g = defaultdict(lambda : None)
    g[(0,0)] = 0
    def grundy(w,b):
        if g[(w,b)] != None:
            return g[(w,b)]
        s = set()
        if w:
            s.add(grundy(w-1,b))
        if b:
            s.add(grundy(w+1,b-1))
        for i in range(1,min(w,b)+1):
            s.add(grundy(w,b-i))
        i = 0
        while i in s:
            i += 1
        g[(w,b)] = i
        return i

    n = I()
    ans = 0
    for _ in range(n):
        w,b = LI()
        ans ^= grundy(w,b)
    print(0 if ans else 1)
    return

#Solve
if __name__ == "__main__":
    solve()

