from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from math import gcd
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gcd
from operator import mul
from functools import reduce


sys.setrecursionlimit(2147483647)
INF = 10 ** 13
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().rstrip().split()
def S(): return sys.stdin.readline().rstrip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]

mod=10**9+7

n=I()
F=sorted(LI(),reverse=True)
flg=[0]*len(F)
flg[0]=1
a=1
flg[0]=1
now=[F[0]]
for i in range(n):
    cnt=0
    for j in range(len(F)):
        if flg[j]==0 and F[j]<now[cnt]:
            cnt+=1
            flg[j]=1
            now+=[F[j]]
        if cnt==a:
            now.sort(reverse=True)
            a*=2
            break
    else:
        print("No")
        exit()

print("Yes")



















