# ABC142 E

f=lambda:map(int,input().split())
N,M=f()
INF=float('inf')

dp=[[INF]*(1<<N) for _ in [0]*(M+1)]
dp[0][0]=0
# dp[m][s]:=n個目まででsを開けるために必要な最小コスト
def list2int(A):
    res=0
    for a in A:
        res+=2**(a-1)
    return res
    
for m in range(M):
    a,b=f()
    c=list2int(list(f()))
    for i in range(1<<N):
        # 次のカギ買った
        dp[m+1][i|c]=min(dp[m][i]+a,dp[m+1][i|c])
        # やめといた
        dp[m+1][i]=min(dp[m][i],dp[m+1][i])
res=dp[M][(1<<N)-1]
print(res if res<INF else -1)