import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def inp():
    return int(input())
def inps():
    return input().rstrip()
def inpl():
    return list(map(int, input().split()))
def _debug(obj):
    print(obj, file=sys.stderr)

# import decimal
# from decimal import Decimal
# decimal.getcontext().prec = 10

# from heapq import heappush, heappop, heapify
# import math
# from math import gcd
# import itertools as it
# import collections
# from collections import deque 

# ---------------------------------------

mod = 2019
S = inps()
dp = [0] * len(S)
mp = {}
ten = 1
for i in range(len(S)-1, -1, -1):
    n = int(S[i])
    if i == len(S) - 1:
        dp[i] = n % mod
    else:
        ten = (ten * 10) % mod
        dp[i] = (dp[i + 1] + n * ten) % mod
    if dp[i] in mp:
        mp[dp[i]] += 1
    else:
        mp[dp[i]] = 1

ans = 0
for k, v in mp.items():
    if k == 0:
        ans += v
    ans += v * (v - 1) // 2
print(ans)
    
