ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
ceil = math.ceil
FT = []
s = input()
x,y = ma()
if s[0]=="T":
    FT.append(0)
prev = s[0]
cnt=0
for i in range(len(s)):
    if s[i]==prev:
        cnt+=1
    else:
        FT.append(cnt)
        cnt=1
    prev=s[i]
FT.append(cnt)
Fxy = [[],[]]
idx=0#0->x 1->y
for i in range(len(FT)):
    if i%2==0:
        Fxy[idx].append(FT[i])
    else:
        if FT[i]%2==0:
            pass
        else:
            idx=(idx+1)%2
def reach(xls,x,f=False):
    l = len(xls)
    su = sum(xls)
    if abs(x) >su:
        return False
    dp = [[False]*(2*su+1) for _ in range(l+1)] #dp[i][j] i 個使ったときにjにいられるか
    dp[0][0] =True

    for i in range(l):
        d = xls[i]
        if i==0 and f:
            if s[0]=="F":
                dp[1][d]=True
                continue
        for j in range(-su,su+1):
            dp[i+1][j] = dp[i][j-d] or dp[i][j+d]
    #print(dp)
    return dp[-1][x]
fx = reach(Fxy[0],x,f=True)
fy = reach(Fxy[1],y)
yn(fx and fy)
#print(FT)
#print(dpx)
#print(dpy)
