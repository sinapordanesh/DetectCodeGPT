def num_unnecessary_cards(N, K, arr):
    def is_good_subset(subset, target):
        dp = [False] * (target + 1)
        dp[0] = True
        for num in subset:
            for i in range(target, num - 1, -1):
                dp[i] |= dp[i - num]
        return dp[target]
    
    unnecessary = 0
    for i in range(N):
        if is_good_subset(arr[:i] + arr[i+1:], K) and not is_good_subset(arr, K):
            unnecessary += 1
    return unnecessary

# Sample Input 1
print(num_unnecessary_cards(3, 6, [1, 4, 3]))

# Sample Input 2
print(num_unnecessary_cards(5, 400, [3, 1, 4, 1, 5]))

# Sample Input 3
print(num_unnecessary_cards(6, 20, [10, 4, 3, 10, 25, 2]))