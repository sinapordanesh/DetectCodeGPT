def examC():
    ans = 0
    print(ans)
    return

def examD():
    ans = 0
    print(ans)
    return

# 解説AC
def examE():
    N = I()
    Bnum = [-1]*N
    Wnum = [-1]*N
    B = {}
    W = {}
    for i in range(2*N):
        c, a = LSI()
        a = int(a)-1
        if c=="W":
            W[i] = a+1
            Wnum[a] = i
        else:
            B[i] = a+1
            Bnum[a] = i
    SB = [[0]*(N*2) for _ in range(N+1)]; SW = [[0]*(N*2) for _ in range(N+1)]
    for i in range(2*N):
        if not i in B:
            continue
        cur = B[i]
        cnt = 0
        SB[cur][i] = 0
        for j in range(2*N):
            if not j in B:
                SB[cur][j] = cnt
                continue
            if B[j]<=cur:
                cnt += 1
            SB[cur][j] = cnt
    for i in range(2*N):
        if not i in W:
            continue
        cur = W[i]
        cnt = 0
        SW[cur][i] = 0
        for j in range(2*N):
            if not j in W:
                SW[cur][j] = cnt
                continue
            if W[j]<=cur:
                cnt += 1
            SW[cur][j] = cnt
    #for b in SB:
        #print(b)
    #print(SW)
    #print(SW,len(SW))

    dp = [[inf]*(N+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        dp[0][i+1] = dp[0][i]+Bnum[i]-SB[i][Bnum[i]]
        dp[i+1][0] = dp[i][0]+Wnum[i]-SW[i][Wnum[i]]
    #print(dp)
    for i in range(N):
        w = Wnum[i]
        for j in range(N):
            b = Bnum[j]
            costb = b - (SB[j][b]+SW[i+1][b])
            costw = w - (SB[j+1][w]+SW[i][w])
            #if i==2 and j==4:
            #    print(w,SB[i][w],SW[j+1][w])
            #    print(b,SB[i][b],SW[j+1][b])
            #print(costb,costw,i,j)
            #input()
            if costb<0:
                costb = 0
                #print(i,j)
            if costw < 0:
                costw = 0
                #print(i,j)
            dp[i+1][j+1] = min(dp[i+1][j+1],dp[i+1][j]+costb,dp[i][j+1]+costw)
    ans = dp[-1][-1]
    #for v in dp:
    #    print(v)
    print(ans)
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