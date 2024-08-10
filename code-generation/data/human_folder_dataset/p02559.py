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
input=sys.stdin.readline
class FenwickTree():
    def __init__(self,n):
        self.n = n
        self.tree = [0]*(n+1)
    def add(self,idx,a):#値の更新
        idx+=1
        while idx<=self.n:
            self.tree[idx] +=a
            idx += idx &-idx

    def _sum(self,r):
        ret=0
        r+=1
        while r>0:
            ret+=self.tree[r]
            r-=r&-r
        return ret
    def sum(self,l,r):
        return self._sum(r)-self._sum(l-1)

n,q = ma()
A = lma()
ft = FenwickTree(n)
for i in range(n):
    ft.add(i,A[i])
for i in range(q):
    t,u,v = ma()
    if t==0:
        ft.add(u,v)
    else:
        print(ft.sum(u,v-1))
