def min_operations(A, B, C):
    nums = [A, B, C]
    max_num = max(nums)
    return sum([(max_num - num) // 2 for num in nums])

# Sample Input 1
print(min_operations(2, 5, 4))

# Sample Input 2
print(min_operations(2, 6, 3))

# Sample Input 3
print(min_operations(31, 41, 5))