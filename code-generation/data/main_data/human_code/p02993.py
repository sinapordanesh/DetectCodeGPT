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

s = v()
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        print("Bad")
        sys.exit()

print("Good")