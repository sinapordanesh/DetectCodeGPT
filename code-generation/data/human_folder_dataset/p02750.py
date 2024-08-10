def examA():
    S = SI()
    if len(S)%2==1:
        print("No")
        return
    for i in range(len(S)//2):
        if S[i*2:i*2+2]!="hi":
            print("No")
            return
    print("Yes")
    return

def examB():
    a, b, M = LI()
    A = LI()
    B = LI()
    D = [LI()for _ in range(M)]
    ans = min(A) + min(B)
    for x,y,c in D:
        cur = A[x-1]+B[y-1]-c
        ans = min(ans,cur)
    print(ans)
    return

def examC():
    def bfs(n, e, fordfs):
        # 点の数、スタートの点、有向グラフ
        W = [-1] * n
        # 各点の状態量、最短距離とか,見たかどうかとか
        W[e] = 0
        que = deque()
        que.append(e)
        while que:
            now = que.popleft()
            nowW = W[now]
            for ne in fordfs[now]:
                if W[ne] == -1:
                    W[ne] = nowW + 1
                    que.append(ne)
        return W
    N = I()
    V = [[]for _ in range(N)]
    for _ in range(N-1):
        a, b = LI()
        a -= 1
        b -= 1
        V[a].append(b)
        V[b].append(a)
    L = bfs(N,0,V)
    #print(L)
    odd = 0
    for l in L:
        if l==-1:
            print(-1)
            return
        if l%2==1:
            odd += 1
    G = []
    if odd*2<N:
        for i in range(N):
            if L[i]%2==1:
                G.append(i)
    else:
        for i in range(N):
            if L[i]%2==0:
                G.append(i)

    used = [False]*(N+1)
    ans = [0]*N
    if N//3>=len(G):
        cur = 3
        for g in G:
            ans[g] = cur
            used[cur] = True
            cur += 3
        cur = 1
        for i in range(N):
            if ans[i]!=0:
                continue
            while(used[cur]):
                cur += 1
            ans[i] = cur
            used[cur] = True
    else:
        cur = 1
        for g in G:
            ans[g] = cur
            used[cur] = True
            cur += 3
            if cur>N:
                cur = 3
        cur = 1
        for i in range(N):
            if ans[i]!=0:
                continue
            while(used[cur]):
                cur += 1
            ans[i] = cur
            used[cur] = True
    print(" ".join(map(str,ans)))
    return

def examD():
    N, T = LI()
    A = []
    A0 = []
    for _ in range(N):
        a, b = LI()
        if a==0:
            A0.append(b)
        else:
            A.append((a/(b+1),a,b))
    A.sort(reverse=True)
    n = len(A)
    S = min(31,n)
    dp = [[inf]*(n+1) for _ in range(S+1)]
    dp[0][0] = 0
    for i,(_,a,b) in enumerate(A):
        for j in range(S):
            now = dp[j][i] + 1
            dp[j][i+1] = min(dp[j][i+1],dp[j][i])
            if now==inf:
                continue
            dp[j+1][i+1] = min(dp[j+1][i+1],now+a*now+b)
    #print(dp)
    dp0 = [0]*(len(A0)+1)
    A0.sort()
    for i,b in enumerate(A0):
        dp0[i+1] = dp0[i]+b+1
    ans = 0
    for i in range(S+1):
        t = T - min(dp[i])
        if t<0:
            break
        cur = (bisect.bisect_right(dp0,t)-1) + i
        if ans<cur:
            ans = cur
    print(ans)
    return

def examE():
    N, M = LI()
    H = 2**N-1; W = 2**M -1
    ans = [[0]*W for _ in range(H)]
    for h in range(H):
        flagh = False
        for m in range(1,11)[::-1]:
            if (h+1)%(2**m)==0:
                flagh = 2**m*2
        for w in range(W):
            flagw = False
            for m in range(1,11)[::-1]:
                if (w+1)%(2**m)==0:
                    flagw = 2 ** m * 2
            if flagh and flagw:
                continue
            ans[h][w] = 1
    for v in ans:
        print("".join(map(str,v)))
    return

def examF():
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
    examD()

"""

"""