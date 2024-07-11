# キャンディーとN人の子供

mod = 10**9 + 7
N, C = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def rev(X):
    return pow(X, mod-2, mod)


pow_sum = [[B[i]-A[i]+1 for j in range(C+1)] for i in range(N)]
pow_table = [[1 for j in range(401)] for i in range(401)]
for i in range(401):
    for j in range(401):
        pow_table[i][j] = pow(i, j, mod)

for cnt in range(C):
    for i in range(N):
        pow_sum[i][cnt+1] = 0
        for j in range(A[i], B[i]+1):
            pow_sum[i][cnt+1] += pow_table[j][cnt+1]
        pow_sum[i][cnt+1] %= mod

ans_dp = [[0 for i in range(C+1)] for j in range(N+1)]
# ans_dp[x][y] = 0<=x<=N,0<=y<=C の場合のdp
ans_dp[0][0] = 1
for n in range(1, N+1):
    # ans_dp[n]の更新
    for c in range(C+1):
        # ans_dp[n][c]の更新
        for k in range(c+1):
            ans_dp[n][c] += ans_dp[n-1][k]*pow_sum[n-1][c-k]
        ans_dp[n][c] %= mod
print(ans_dp[N][C] % mod)