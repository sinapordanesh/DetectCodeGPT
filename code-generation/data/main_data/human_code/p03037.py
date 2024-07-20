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
inf = float("inf")
al = "abcdefghijklmnopqrstuvwxyz"
AL = al.upper()

N, M = I()
count = 0
 
min_a = 1
max_b = N
 
for i in range(M):
    a,b = [int(i) for i in input().split()]
    if min_a < a:
        min_a = a
    if max_b > b:
        max_b = b
 
print(max(0, max_b-min_a+1))