def max_sum_utilities(N, K, integers):
    dp = [-1] * (K + 1)
    dp[0] = 0
    
    for i in range(N):
        a, b = integers[i]
        for j in range(K, -1, -1):
            if dp[j] != -1:
                if dp[j] >= a:
                    dp[j] = max(dp[j], dp[j] - a + b)
                else:
                    dp[j | a] = max(dp[j | a], dp[j] + b)
    
    return max(dp)

# Read inputs
N, K = map(int, input().split())
integers = [tuple(map(int, input().split())) for _ in range(N)]

# Call the function and print the result
print(max_sum_utilities(N, K, integers))