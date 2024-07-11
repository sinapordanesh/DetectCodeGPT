def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())

n=int(input())
ar=lis()
data=[]
for i in range(n):
    data.append((ar[i],i))
data.sort(reverse=True)
dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    a, p = data[i]
    for j in range(i+1):
        dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j] + abs(n-1-j-p)*a)
        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + abs(i-j-p)*a)
#print(dp)
print(max(dp[-1]))






