def find_max_height(N, K, heights):
    current_height = K
    for height in heights:
        if height < current_height:
            current_height += 1
    return current_height - K

# Sample Input 1
print(find_max_height(5, 5, [3949, 3774, 3598, 3469, 3424]))

# Sample Input 2
print(find_max_height(5, 3, [7, 4, 2, 6, 4]))