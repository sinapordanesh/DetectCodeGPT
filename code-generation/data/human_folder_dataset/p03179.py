def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())
def inp():
    return input()

N=10**9 +7
n=int(inp())
s=inp()
dp=[[0]*(n+1) for _ in range(n+1)]#base 1 indexing
dp[1][1]=1
for i in range(2,n+1):
    pref=[0]
    for t in range(1,i):
        pref.append((pref[-1]+dp[i-1][t])%N)
    for j in range(1,i+1):


        if s[i-2]==">":
            l=j
            r=i-1
        else:

            l=1
            r=j-1

        if l>r:
            continue
        dp[i][j]=((pref[r]-pref[l-1])%N + N)%N
ans=0
for i in range(1,n+1):
    ans=(ans+dp[n][i])%N

print(ans)


