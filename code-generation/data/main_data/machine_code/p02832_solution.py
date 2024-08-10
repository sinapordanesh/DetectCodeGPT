def min_bricks_to_break(N, arr):
    unique_nums = set(arr)
    if len(unique_nums) != N:
        return N - len(unique_nums)
    else:
        return -1

# Sample Input 1
print(min_bricks_to_break(3, [2, 1, 2]))

# Sample Input 2
print(min_bricks_to_break(3, [2, 2, 2]))

# Sample Input 3
print(min_bricks_to_break(10, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))

# Sample Input 4
print(min_bricks_to_break(1, [1]))