def min_unbalancedness():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [list(map(int, input().split())) for _ in range(H)]
    
    dp = [[[float('inf')] * (sum(sum(row) for row in B) + 1) for _ in range(W)] for _ in range(H)]
    dp[0][0][A[0][0]] = B[0][0]
    dp[0][0][B[0][0]] = A[0][0]
    
    for i in range(H):
        for j in range(W):
            for k in range(sum(sum(row) for row in B) + 1):
                if i < H - 1:
                    dp[i + 1][j][k + A[i + 1][j]] = min(dp[i + 1][j][k + A[i + 1][j]], dp[i][j][k] + B[i + 1][j])
                    dp[i + 1][j][k + B[i + 1][j]] = min(dp[i + 1][j][k + B[i + 1][j]], dp[i][j][k] + A[i + 1][j])
                if j < W - 1:
                    dp[i][j + 1][k + A[i][j + 1]] = min(dp[i][j + 1][k + A[i][j + 1]], dp[i][j][k] + B[i][j + 1])
                    dp[i][j + 1][k + B[i][j + 1]] = min(dp[i][j + 1][k + B[i][j + 1]], dp[i][j][k] + A[i][j + 1])
    
    res = float('inf')
    for k in range(sum(sum(row) for row in B) + 1):
        res = min(res, max(k, sum(sum(row) for row in B) - k) - dp[H - 1][W - 1][k])
    
    print(res)

min_unbalancedness()