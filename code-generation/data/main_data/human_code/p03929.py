def examA():
    N, L = LI()
    V, D = LI()
    X = [LI()for _ in range(N)]

    ans = 0
    print(ans)
    return

def examB():
    N, K = LI()
    H = 11; W = 7
    S = [[0]*(W+1) for _ in range(H+3)]
    for h in range(H+2):
        for w in range(W):
            S[h+1][w+1] = (S[h][w+1] + S[h+1][w] - S[h][w] + (7*h+w+1))
    #print(S)
    base = 0
    for h in range(H):
        for w in range(W-2):
            cur = S[h+3][w+3] - S[h+3][w] - S[h][w+3] + S[h][w]
            if cur%11==K:
                base += 1
                #print(h,w)
    ans = base * ((N-2)//11)
    #print(ans)
    rest = (N-2)%11
    for h in range(rest):
        for w in range(W-2):
            cur = S[h+3][w+3] - S[h+3][w] - S[h][w+3] + S[h][w]
            if cur%11==K:
                ans += 1
                #print(h,w)
    print(ans)
    return

def examC():
    ans = 0
    print(ans)
    return

def examD():
    ans = 0
    print(ans)
    return

import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    examB()

"""

"""