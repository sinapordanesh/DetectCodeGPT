import sys
from sys import exit
from collections import deque
from bisect import bisect_left, bisect_right, insort_left, insort_right #func(リスト,値)
from heapq import heapify, heappop, heappush
from math import *

sys.setrecursionlimit(10**6)
INF = 10**20
eps = 1.0e-20
MOD = 10**9+7

def mint():
    return map(int,input().split())
def lint():
    return list(map(int,input().split()))
def ilint():
    return int(input()), list(map(int,input().split()))
def judge(x, l=['Yes', 'No']):
    print(l[0] if x else l[1])
def lprint(l, sep='\n'):
    for x in l:
        print(x, end=sep)

N,M = mint()
if N==M==1:
    print(1)
else:
    print(abs(N-2)*abs(M-2))