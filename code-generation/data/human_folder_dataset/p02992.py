def guchoku(n,k,mod):
    dp=[1]*(n+1)
    dp[0]=0
    for _ in range(k-1):
        ndp=[0]*(n+1)
        for i in range(1,n+1):
            ndp[i]+=sum([dp[j+1] for j in range(n//i)])
            ndp[i]%=mod
        dp=ndp.copy()
    return sum(dp)%mod
def main(n,k,mod):
    ary=[]
    tmp=0
    for i in range(1,int(n**0.5)+1):
        ary.append(n//i-n//(i+1))
        tmp+=ary[-1]
    tmp=n-tmp
    ary+=[1]*tmp
    ary.reverse()
    dp=[x for x in ary]
    m=len(ary)
    for i in range(m-1):
        dp[i+1]+=dp[i]
        dp[i+1]%=mod
    for _ in range(k-1):
        ndp=[0]*m
        for i in range(m):
            ndp[i]+=dp[-i-1]*ary[i]
            ndp[i]%=mod
            pass
        for i in range(m-1):
            ndp[i+1]+=ndp[i]
            ndp[i+1]%=mod
        dp=[x for x in ndp]
    return dp[-1]

n,k=map(int,input().split())
mod=10**9+7
#print(guchoku(n,k,mod))
print(main(n,k,mod))