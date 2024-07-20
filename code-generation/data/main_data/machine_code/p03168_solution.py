def more_heads_than_tails():
    N, *p = map(float, input().split())
    
    dp = [0.0] * (N+1)
    dp[0] = 1.0
    
    for i in range(N):
        for j in range(i+1, -1, -1):
            dp[j] = (1-p[i]) * dp[j] + p[i] * dp[j-1]
    
    result = sum(dp[(N+1)//2:])
    print("{:.9f}".format(result))

more_heads_than_tails()