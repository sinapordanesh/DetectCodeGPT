def maximum_utility(N, K, integers):
    dp = [-1] * (K + 1)
    dp[0] = 0
    
    for i in range(N):
        new_dp = dp.copy()
        a, b = integers[i]
        for j in range(K):
            if dp[j] >= 0:
                if dp[j] >= b:
                    new_dp[j | a] = max(new_dp[j | a], dp[j])
                else:
                    new_dp[j | a] = max(new_dp[j | a], dp[j] + b)
        dp = new_dp
    
    return max(dp)

# Input
N, K = map(int, input().split())
integers = [list(map(int, input().split())) for _ in range(N)]

# Call the function and print the output
print(maximum_utility(N, K, integers))