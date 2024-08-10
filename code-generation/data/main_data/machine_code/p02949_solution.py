def maximum_score(N, M, P, edges):
    dp = [-float('inf')] * (N + 1)
    dp[1] = 0
    
    for _ in range(N):
        for a, b, c in edges:
            dp[b] = max(dp[b], dp[a] + c - P)
    
    for _ in range(N):
        for a, b, c in edges:
            if dp[a] + c - P > dp[b]:
                dp[b] = float('inf')
    
    return dp[N] if dp[N] != float('inf') else -1

# Sample Input 1
print(maximum_score(3, 3, 10, [(1, 2, 20), (2, 3, 30), (1, 3, 45)])) # Output: 35

# Sample Input 2
print(maximum_score(2, 2, 10, [(1, 2, 100), (2, 2, 100)])) # Output: -1

# Sample Input 3
print(maximum_score(4, 5, 10, [(1, 2, 1), (1, 4, 1), (3, 4, 1), (2, 2, 100), (3, 3, 100)])) # Output: 0