from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush,heappop,heapify
import math
from collections import *
from functools import reduce,cmp_to_key
import sys
input = sys.stdin.readline

from itertools import accumulate
from functools import lru_cache

M = mod = 10 ** 9 + 7
def factors(n):return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def inv_mod(n):return pow(n, mod - 2, mod)
 
def li():return [int(i) for i in input().rstrip('\n').split()]
def st():return input().rstrip('\n')
def val():return int(input().rstrip('\n'))
def li2():return [i for i in input().rstrip('\n')]
def li3():return [int(i) for i in input().rstrip('\n')]
 



sys.setrecursionlimit(10 ** 6)

g = 0
@lru_cache(None)
def dp(i, par = -1, black = 0):
    global g
    ans = 1
    nokids = 1
    if black:
        for j in g[i]:
            if j != par:
                nokids = 0
                ans = ans * dp(j, i, 0) % mod
    else:
        for j in g[i]:
            if j != par:
                nokids = 0
                ans = ( ans * (dp(j, i, 0) + dp(j, i, 1)) ) % mod

    if nokids:ans = 1
    return ans



n = val()
g = [[] for i in range(n + 1)]

l = []
for _ in range(n - 1):
    a, b = li()
    g[a].append(b)
    g[b].append(a)


root = 1    
ans = dp(root, -1, 0) + dp(root, -1, 1)

print(ans % mod)
