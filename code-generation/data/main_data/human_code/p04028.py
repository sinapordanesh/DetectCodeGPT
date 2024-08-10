def main():
  mod=10**9+7
  n=int(input())
  m=len(input())
  dp=[[0]*(n+1) for _ in range(2)]
  dp[0][0]=1
  for i in range(n):
    for j in range(n+1):
      dp[(i+1)&1][j]=0
    for j in range(n):
      dp[(i+1)&1][j+1]=(dp[i&1][j]+dp[(i+1)&1][j+1])%mod
      dp[(i+1)&1][j]=(dp[(i+1)&1][j]+dp[i&1][j+1]*2)%mod
    dp[(i+1)&1][0]=(dp[(i+1)&1][0]+dp[i&1][0])%mod
  print(dp[n&1][m])
main()