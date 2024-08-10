import sys
input = sys.stdin.readline

mod = 10**9+7



# (i, j, k+1)に置くのが、条件(l,x)に適しているか
def check(i, j, l, x):
    return (x == 3 and l <= i) or (x == 2 and i < l <= j) or (x == 1 and j < l)


N, M = map(int, input().split())
LRX = [list(map(int, input().split())) for _ in range(M)]

LX = [[] for _ in range(N+2)]
for l, r, x in LRX:
    LX[r].append((l, x))

dp = [[[0]*(j+1) for j in range(i+1)] for i in range(N+2)]
# dp[i][j][k] (k <= j <= i) 
# 三色それぞれ、最後に使ったindex(1-indexed)がi,j,k

dp[0][0][0] = 1

for i in range(N+1):
    for j in range(i, N+1):
        for k in range(j, N+1):
            
            # 一番前の色を置く
            ok = True
            for l, x in LX[k+1]:
                if not check(j, k, l, x):
                    ok = False
                    break
            if ok:
                dp[k+1][k][j] = (dp[k+1][k][j] + dp[k][j][i]) % mod
            
            # 最後
            ok = True
            for l, x in LX[k+1]:
                if not check(i, j, l, x):
                    ok = False
                    break
            if ok:
                dp[k+1][j][i] = (dp[k+1][j][i] + dp[k][j][i]) % mod
            
            # 二番目
            ok = True
            for l, x in LX[k+1]:
                if not check(i, k, l, x):
                    ok = False
                    break
            if ok:
                dp[k+1][k][i] = (dp[k+1][k][i] + dp[k][j][i]) % mod
        

ans = 0
for a in range(N+1):
    for b in range(a,N+1):
        ans = (ans + dp[N][b][a]) % mod

print(ans)
