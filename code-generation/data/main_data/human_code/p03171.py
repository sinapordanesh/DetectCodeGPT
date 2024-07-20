def coun(a,i,j):
    if dp[i][j]!=-1:
        return dp[i][j]

    if i==j:
        return a[i]
    elif abs(i-j)==1:

        return max(a[i],a[j])
    dp[i][j]= max(min(coun(a,i+2,j),coun(a,i+1,j-1))+a[i],min(coun(a,i+1,j-1),coun(a,i,j-2))+a[j])

    return dp[i][j]

n= int(input())
a =[int(X ) for  X in input().split()]
dp = [[-1 for i in range(n)]for j in range(n)]
print(2*coun(a,0,n-1)-sum(a))