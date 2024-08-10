def newspaper_subscriptions(N, A, B):
    max_subscriptions = min(A, B)
    min_subscriptions = max(0, A + B - N)
    
    return max_subscriptions, min_subscriptions

# Sample Input 1
print(newspaper_subscriptions(10, 3, 5)) # Output: (3, 0)

# Sample Input 2
print(newspaper_subscriptions(10, 7, 5)) # Output: (5, 2)

# Sample Input 3
print(newspaper_subscriptions(100, 100, 100)) # Output: (100, 100)