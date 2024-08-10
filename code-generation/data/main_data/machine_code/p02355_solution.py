def smallest_window(arr, K):
    n = len(arr)
    freq = [0] * (K+1)
    unique = 0
    left = 0
    min_len = float('inf')
    
    for right in range(n):
        if freq[arr[right]] == 0:
            unique += 1
        freq[arr[right]] += 1
        
        while unique == K:
            min_len = min(min_len, right - left + 1)
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                unique -= 1
            left += 1
    
    if min_len == float('inf'):
        return 0
    else:
        return min_len
    
# Sample Input
print(smallest_window([4, 1, 2, 1, 3, 5], 2)) # Output: 2
print(smallest_window([4, 1, 2, 1, 3, 5], 3)) # Output: 3
print(smallest_window([1, 2, 3], 4)) # Output: 0