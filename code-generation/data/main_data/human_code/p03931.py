
n,K=map(int,input().split())
lists=list(map(int,input().split()))
mod=10**9+7
dp=[[["inf" for i in range(256)] for j in range(n+1)] for k in range(n+1)]
#dp[i][j][k]=カードのi番目までからjこまでを取ってxorの値をkにする方法
#dp[i][j]=="inf" (i<jの時)
for i in range(n+1):
    dp[i][0][0]=1
for i in range(1,n+1):
    num=lists[i-1]
    for j in range(1,i+1):
        for k in range(256):
            if dp[i-1][j-1][k^num]!="inf" or dp[i-1][j][k]!="inf": 
                s=0
                if dp[i-1][j][k]!="inf":
                    s+=dp[i-1][j][k]
                if dp[i-1][j-1][k^num]!="inf":
                    s+=dp[i-1][j-1][k^num]
                dp[i][j][k]=s%mod
            else:
                pass
ans=0
def find_power(n,mod):
    # 0!からn!までのびっくりを出してくれる関数(ただし、modで割った値に対してである）
    powlist=[0]*(n+1)
    powlist[0]=1
    powlist[1]=1
    for i in range(2,n+1):
        powlist[i]=powlist[i-1]*i%(mod)
    return powlist
A=find_power(100,mod)

for i in range(n+1):
    if dp[n][i][K]!="inf":
        ans+=dp[n][i][K]*A[i]
        ans=ans%mod
print(ans)