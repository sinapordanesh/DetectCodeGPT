def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())


n,s=sep()
ar=lis()
ar.insert(0,0)
dp=[[0]*(s+2) for _ in range(n+2)]
dp[0][0]=1
N=998244353
for i in range(1,n+1):
    for j in range(0,s+1):
        dp[i][j]=(2*dp[i-1][j])%N
        if j-ar[i]>=0:
            dp[i][j]=(dp[i][j]+dp[i-1][j-ar[i]])%N
#print(dp)
print(dp[n][s])

