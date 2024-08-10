def longest_increasing_subsequence(n, arr):
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp) if dp else 0

# Sample Input
print(longest_increasing_subsequence(5, [5, 1, 3, 2, 4])) # Output: 3
print(longest_increasing_subsequence(3, [1, 1, 1])) # Output: 1