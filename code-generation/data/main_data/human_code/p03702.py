ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
ips = lambda:input().split()
import collections
import math
import itertools
import heapq as hq
import sys
ceil=math.ceil
n,a,b = ma()
H = []
for i in range(n):
    H.append(ni())
H.sort()
def isok(x):
    bs = b*x
    d=a-b
    cnt=0
    for h in H:
        if h>bs:
            cnt+=math.ceil((h-bs)/d)
    return cnt<=x

def bisect():
    ok = 10**9
    ng = 0
    x = (ok+ng)//2
    while ok-ng>1:
        if isok(x):
            ok=x
        else:
            ng=x
        x=(ok+ng)//2
    return ok
print(bisect())
