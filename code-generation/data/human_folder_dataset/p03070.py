import sys
def I(): return int(sys.stdin.readline().rstrip())


N = I()
A = [0] + [I() for _ in range(N)]
s = sum(A)
mod = 998244353

dp1 = [[0]*(s+1) for _ in range(N+1)]  # dp[i][j] = a1~aiを塗った時に、赤で塗った和をjにする方法数
dp1[0][0] = 1
for i in range(1,N+1):
    a = A[i]
    for j in range(s+1):
        if j >= a:
            dp1[i][j] = dp1[i-1][j]*2 + dp1[i-1][j-a]
        else:
            dp1[i][j] = dp1[i-1][j]*2
        dp1[i][j] %= mod

dp2 = [[0]*(s//2+1) for _ in range(N+1)]  # dp[i][j] = a1~aiの中からいくつか選んで、和をjにする方法数
dp2[0][0] = 1
for i in range(1,N+1):
    a = A[i]
    for j in range(s//2+1):
        if j >= a:
            dp2[i][j] = dp2[i-1][j] + dp2[i-1][j-a]
        else:
            dp2[i][j] = dp2[i-1][j]
        dp2[i][j] %= mod

a = sum(dp1[N][i] for i in range((s+1)//2,s+1))
a %= mod
if s % 2 == 0:
    a -= dp2[N][s//2]

ans = pow(3,N,mod)-a*3
ans %= mod
print(ans)
