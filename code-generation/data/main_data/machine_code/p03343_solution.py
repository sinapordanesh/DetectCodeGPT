def smallest_difference(N, K, Q, A):
    def find_largest_smallest_remove(nums):
        smallest = min(nums)
        largest = max(nums)
        return largest, smallest
    
    min_diff = float('inf')
    
    for i in range(N - Q + 1):
        subsequence = A[i:i+Q]
        largest, smallest = find_largest_smallest_remove(subsequence)
        min_diff = min(min_diff, largest - smallest)
    
    return min_diff

# Sample Input 1
print(smallest_difference(5, 3, 2, [4, 3, 1, 5, 2]))

# Sample Input 2
print(smallest_difference(10, 1, 6, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]))

# Sample Input 3
print(smallest_difference(11, 7, 5, [24979445, 861648772, 623690081, 433933447, 476190629, 262703497, 211047202, 971407775, 628894325, 731963982, 822804784]))