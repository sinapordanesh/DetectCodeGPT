def replace_elements(n, arr):
    count = 0
    unique_nums = set(arr)
    if len(unique_nums) == 1:
        return n // 2
    for i in range(n-2):
        if arr[i] == arr[i+2]:
            count += 1
    return count

# Sample Input 1
print(replace_elements(4, [3, 1, 3, 2])) 

# Sample Input 2
print(replace_elements(6, [105, 119, 105, 119, 105, 119]))

# Sample Input 3
print(replace_elements(4, [1, 1, 1, 1]))