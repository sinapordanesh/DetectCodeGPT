def examA():
    def gcd(x, y):
        if y == 0:
            return x
        while (y != 0):
            x, y = y, x % y
        return x
    def lcm(x, y):
        return x * y // gcd(x, y)
    N, Z = LI()
    A = LI()
    F = set()
    for a in A:
        F.add(gcd(a,Z))
    #print(F)
    ans = 1
    for f in F:
        ans = lcm(f,ans)

    print(ans)
    return

def examB():
    ans = 0
    print(ans)
    return

def examC():
    ans = [[0]*3 for _ in range(3)]
    ans[0][0] = I()
    ans[0][1] = I()
    ans[1][1] = I()
    center = ans[1][1]
    ans[2][2] = center*2-ans[0][0]
    ans[0][2] = center*3-sum(ans[0])
    ans[1][2] = center*3-ans[0][2]-ans[2][2]
    ans[1][0] = center*2-ans[1][2]
    ans[2][0] = center*3-ans[1][0]-ans[0][0]
    ans[2][1] = center*3-ans[2][0]-ans[2][2]
    for v in ans:
        print(" ".join(map(str,v)))
    return

def examD():
    ans = 0
    print(ans)
    return

def examE():
    ans = 0
    print(ans)
    return

from decimal import Decimal as dec
import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
def LI(): return list(map(int,sys.stdin.readline().split()))
def DI(): return dec(input())
def LDI(): return list(map(dec,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examC()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""