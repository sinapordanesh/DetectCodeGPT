import re
import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
import functools
def v(): return input()
def k(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def X(): return list(input())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 6)
mod = 10**9+7
cnt = 0
ans = 0
num = []
inf = float("inf")
al = "abcdefghijklmnopqrstuvwxyz"
AL = al.upper()

N = k()
if N == 1:
    print(1)
    sys.exit()
 
for i in range(N,-1,-1):
    for j in range(1,int(N**0.5)+1):
        for k in range(2,11):
            if j**k == i:
                print(i)
                sys.exit()