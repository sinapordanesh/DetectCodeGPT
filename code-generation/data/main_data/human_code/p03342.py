import bisect, copy, heapq, math, sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
def celi(a,b):
    return -(-a//b)
sys.setrecursionlimit(5000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n=int(input())
a=list(map(int,input().split()))
ans=0
l,r=0,0
cnt=0
xor=0
for i in range(n):
    l=i
    if l==r:
        cnt+=a[i]
        xor+=a[i]
        r+=1
    while r+1<=n and xor^a[r]==cnt+a[r]:
        xor^=a[r]
        cnt+=a[r]
        r+=1
    # print(l,r,cnt,xor)
    cnt-=a[i]
    xor-=a[i]
    ans+=r-l
print(ans)