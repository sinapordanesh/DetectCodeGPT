# -*- coding: utf-8 -*-

from heapq import heappush, heappop

import sys
sys.setrecursionlimit(10 ** 9)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

que=[]
while True:
    instr=input()
    if instr.startswith('insert'):
        _,n=instr.split()
        heappush(que, -int(n))
    elif instr.startswith('extract'):
        print(-heappop(que))
    else:
        break

