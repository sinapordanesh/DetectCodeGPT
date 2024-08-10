def main(n,A,B):
  AB=[[a,b] for a,b in zip(A,B)]
  dp=[0]*(n+1)
  dp[0]=n
  # dp[i]:どんぐりをi個交換した時の最大獲得どんぐり
  for a,b in AB:
    #if a>b:continue
    ddp=[0]*(n+1)
    ddp[0]=n
    for i in range(n+1):
      ddp[i]=max(dp[i],ddp[i-a]+b-a if i-a>=0 else 0)
    dp=ddp
  n=max(dp)
  dp=[0]*(n+1)
  dp[0]=n
  for a,b in AB:
    if b>a:continue
    ddp=[0]*(n+1)
    ddp[0]=n
    for i in range(n+1):
      ddp[i]=max(dp[i],ddp[i-b]+a-b if i-b>=0 else 0)
    dp=ddp
  return max(dp)

n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
print(main(n,A,B))
