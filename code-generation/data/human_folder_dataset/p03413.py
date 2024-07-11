def examC():
    ans = 0
    print(ans)
    return

def examD():
    ans = 0
    print(ans)
    return

def examE():
    N = I()
    A = LI()
    ans = -inf

    S = [0]*(N+1)
    fr = [-1]*N
    best = -1

    for i,a in enumerate(A):
        S[i] = a
        for j in range(i):
            if ((i-j)%2==0):
                if (S[j]+a>S[i]):
                    fr[i] = j
                    S[i] = S[j] + a
            if (S[i]>ans):
                ans = S[i]
                best = i
    #print(best)
    V = []
    for i in range(best+1,N)[::-1]:
        V.append(i+1)
    i = best
    while(fr[i]>=0):
        f = fr[i]
        #print(i,f)
        while(f<i):
            V.append(1+(i+f)//2)
            i -= 2
    for _ in range(i):
        V.append(1)

    print(ans)
    print(len(V))
    for v in V:
        print(v)
    return

def examF():
    ans = 0
    print(ans)
    return

from decimal import getcontext,Decimal as dec
import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
def LI(): return list(map(int,sys.stdin.readline().split()))
def DI(): return dec(input())
def LDI(): return list(map(dec,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = dec("0.000000000001")
alphabet = [chr(ord('a') + i) for i in range(26)]
alphabet_convert = {chr(ord('a') + i): i for i in range(26)}

getcontext().prec = 28

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examE()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""