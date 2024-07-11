from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
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
A=LI()
c=1
for i in range(2,n+1):
    c=c*i%mod

C=[0]*(n+2)
ret=c
for i in range(2,n+1):
    C[i]=c*pow(i,mod-2,mod)%mod
    ret+=C[i]
    ret%=mod

ans=0
for j in range(n):
    ans+=ret*A[j]%mod
    ans%=mod
    ret-=C[n-j]
    ret+=C[j+2]

print(ans)