def max_sum(R, C, K, items):
    dp = [[0] * 4 for _ in range(R+1)]
    
    for r, c, v in items:
        next_dp = [[0] * 4 for _ in range(R+1)]
        for i in range(1, R+1):
            for j in range(1, 4):
                next_dp[i][j] = max(next_dp[i][j], dp[i][j])
                if i == r:
                    next_dp[i][j] = max(next_dp[i][j], dp[i][j-1] + v)
                else:
                    next_dp[i][1] = max(next_dp[i][1], dp[i][j] + v)
        
        dp = next_dp
    
    return max(dp[R])

R, C, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(K)]

print(max_sum(R, C, K, items))