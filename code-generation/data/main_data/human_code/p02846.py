from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

t = inpl()
a = inpl()
b = inpl()
if (a[0] > b[0] and a[1] > b[1]) or (a[0] < b[0] and a[1] < b[1]):
    print(0)
    quit()
c = [0,0]
for i in range(2):
    c[i] = abs(a[i]-b[i]) * t[i]
if c[0] == c[1]:
    print('infinity')
    quit()
if c[0] > c[1]:
    print(0)
else:
    sa = c[1]-c[0]
    tmp = 0
    if c[1]%sa:
        tmp = 1
    print((c[1]-1)//(c[1]-c[0])*2 - tmp)
