import sys
from itertools import accumulate
import math

def main():
  input=sys.stdin.readline
  n=int(input())
  A=list(map(int,input().split()))
  dp=[[math.inf]*n for _ in range(n)]
  for i in range(n):
    dp[i][i]=0
  #print(*dp,sep="\n")
  accA=list(accumulate([0]+A))
  #print(accA)
  for L in reversed(range(n)):
    dpL=dp[L]
    for R in range(L+1,n):
      dpL[R]=min([dpL[k-1]+dp[k][R] for k in range(L+1,R+1)])+accA[R+1]-accA[L]
  #print(dp)
  print(dp[0][-1])
main()