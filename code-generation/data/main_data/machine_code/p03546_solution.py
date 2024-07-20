def magical_girl(H, W, c, A):
    INF = 10**9
    dp = [[INF]*10 for _ in range(10)]
    for i in range(10):
        for j in range(10):
            dp[i][j] = min(dp[i][j], c[i][j])
    
    for k in range(10):
        for i in range(10):
            for j in range(10):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    
    ans = 0
    for i in range(H):
        for j in range(W):
            if A[i][j] != -1:
                ans += dp[A[i][j]][1]
    
    return ans

# Sample Input 1
H, W = 2, 4
c = [[0, 9, 9, 9, 9, 9, 9, 9, 9, 9],
     [9, 0, 9, 9, 9, 9, 9, 9, 9, 9],
     [9, 9, 0, 9, 9, 9, 9, 9, 9, 9],
     [9, 9, 9, 0, 9, 9, 9, 9, 9, 9],
     [9, 9, 9, 9, 0, 9, 9, 9, 9, 2],
     [9, 9, 9, 9, 9, 0, 9, 9, 9, 9],
     [9, 9, 9, 9, 9, 9, 0, 9, 9, 9],
     [9, 9, 9, 9, 9, 9, 9, 0, 9, 9],
     [9, 9, 9, 9, 2, 9, 9, 9, 0, 9],
     [9, 2, 9, 9, 9, 9, 9, 9, 9, 0]]
A = [[-1, -1, -1, -1],
     [8, 1, 1, 8]]

print(magical_girl(H, W, c, A))