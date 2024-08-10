from heapq import *
import sys
from collections import *
from itertools import *
from decimal import *
import copy
from bisect import *
import math
import random
sys.setrecursionlimit(4100000)
def gcd(a,b):
    if(a%b==0):return(b)
    return (gcd(b,a%b))
input=lambda :sys.stdin.readline().rstrip()



N=int(input())
mod=10**9+7
dp=[[8,1,1,0] for i in range(N)]#1,2~8,9,both
for i in range(1,N):
    dp[i][0]=dp[i-1][0]*8
    dp[i][1]=dp[i-1][0]+dp[i-1][1]*9
    dp[i][2]=dp[i-1][0]+dp[i-1][2]*9
    dp[i][3]=dp[i-1][1]+dp[i-1][2]+dp[i-1][3]*10
    for n in range(4):
        dp[i][n]%=mod
print(dp[-1][3]%mod)
