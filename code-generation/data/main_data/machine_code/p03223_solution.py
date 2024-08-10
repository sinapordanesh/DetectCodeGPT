def max_sum_adjacent_diff(N, nums):
    nums.sort()
    max_sum = 0
    for i in range(N-1):
        max_sum += abs(nums[i] - nums[i+1])
    return max_sum

# Sample Input 1
print(max_sum_adjacent_diff(5, [6, 8, 1, 2, 3]))

# Sample Input 2
print(max_sum_adjacent_diff(6, [3, 1, 4, 1, 5, 9]))

# Sample Input 3
print(max_sum_adjacent_diff(3, [5, 5, 1]))