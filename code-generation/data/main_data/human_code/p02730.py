import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy,bisect
from operator import itemgetter
#from heapq import heappush, heappop
#import numpy as np
#from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
#from scipy.sparse import csr_matrix
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
nf = lambda: float(ns())
na = lambda: list(map(int, stdin.readline().split()))
nb = lambda: list(map(float, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

def judge(S):
    for i in range(len(S) // 2):
        if S[i] != S[-(i+1)]:
            return False
    return True

S = ns()
N = len(S)
p = S[:(N-1)//2]
l = S[(N+3)//2 - 1:]
if judge(S) and judge(p) and judge(l):
    print('Yes')
else:
    print('No')

