def max_shopping(N, T, stores):
    stores.sort(key=lambda x: (x[0], -x[1]))
    ans = 0
    dp = [0] * (T + 1)
    
    for a, b in stores:
        for i in range(T, -1, -1):
            if i + a <= T:
                dp[i + a] = max(dp[i + a], dp[i] + b)
    
    for a, b in stores:
        for i in range(T):
            ans = max(ans, dp[i] + a * i + b)
    
    return ans

# Input
N = 3
T = 7
stores = [(2, 0), (3, 2), (0, 3)]
print(max_shopping(N, T, stores))