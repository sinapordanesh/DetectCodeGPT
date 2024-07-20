def examA():
    ABC =LI(); ABC.sort()
    if ABC[0]==ABC[-1]:
        print("Yes")
    else:
        print("No")
    return

def examB():
    N = I()
    S = SI()
    red = S.count("R")
    if red>N//2:
        print("Yes")
    else:
        print("No")
    return

def examC():
    N,Q = LI()
    S = SI()
    T = [LSI()for _ in range(Q)]
    l = -1; r = N
    while(r-l>1):
        cur = (r+l)//2
        now = copy.deepcopy(cur)
        flag = False
        for t,d in T:
            if S[now]==t:
                if d=="R":
                    now += 1
                else:
                    now -= 1
            if now==N:
                flag = True
                break
            if now==-1:
                break
        if flag:
            r = cur
        else:
            l = cur
    R = r
    l = -1; r = N
    while(r-l>1):
        cur = (r+l)//2
        now = copy.deepcopy(cur)
        flag = False
        for t,d in T:
            if S[now]==t:
                if d=="R":
                    now += 1
                else:
                    now -= 1
            if now==-1:
                flag = True
                break
            if now==N:
                break
        if flag:
            l = cur
        else:
            r = cur
    L = l
    ans = max(0,R-L-1)
    print(ans)
    return

def examD():
    N, X = LI()
    S = LI()
    S.sort(reverse=True)
    dp = [[0]*(X+1)for _ in range(N+1)]
    dp[0][X] = 1
    for i in range(N):
        s = S[i]
        for j in range(X+1):
            dp[i+1][j%s] += dp[i][j]
            dp[i+1][j%s] %= mod
        for j in range(X+1):
            dp[i+1][j] += dp[i][j]*(N-i-1)
            dp[i+1][j] %= mod
    #print(dp)
    ans = 0
    for i,d in enumerate(dp[-1]):
        ans += d*i
        ans %= mod
    print(ans)
    return

def examE():
    ans = 0
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    examD()

"""

"""