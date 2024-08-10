def find_minimum_total_cost():
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        
        towns = []
        for _ in range(n):
            d, e = map(int, input().split())
            towns.append((d, e))
        
        roads = []
        for _ in range(m):
            a, b, c = map(int, input().split())
            roads.append((a, b, c))
        
        dp = [[float('inf')] * n for _ in range(2)]
        dp[0][0] = 0
        
        for _ in range(2 * n):
            for a, b, c in roads:
                dp[1][b] = min(dp[1][b], dp[0][a] + c + towns[b-1][0])
            
            if dp[0] == dp[1]:
                break
            dp[0] = dp[1][:]
        
        if dp[1][n-1] == float('inf'):
            print(-1)
        else:
            print(dp[1][n-1])


find_minimum_total_cost()