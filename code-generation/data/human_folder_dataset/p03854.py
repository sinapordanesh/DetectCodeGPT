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
rev=s[::-1]
can='YES'
while(len(rev)!=0):
    if(rev[:3]=='rem'):
        if(rev[:7]=='remaerd'):
            rev=rev[7:]

        else:
            can='NO'
            break
    
    elif(rev[:3]=='res'):
        if(rev[:6]=='resare'):
            rev=rev[6:]

        else:
            can='NO'
            break
    
    elif(rev[0]=='e'):
        if(rev[:5]=='esare'):
            rev=rev[5:]

        else:
            can='NO'
            break
    elif(rev[0]=='m'):
        if(rev[:5]=='maerd'):
            rev=rev[5:]

        else:
            can='NO'
            break
    else:
        can='NO'
        break

print(can)

