def min_elements_to_replace(n, v):
    count = 0
    unique_nums = set(v)
    
    if len(unique_nums) <= 2:
        return 0
    
    for i in range(n-2):
        if v[i] == v[i+2]:
            continue
        else:
            count += 1
    
    return count

# Sample Input 1
print(min_elements_to_replace(4, [3, 1, 3, 2]))

# Sample Input 2
print(min_elements_to_replace(6, [105, 119, 105, 119, 105, 119]))

# Sample Input 3
print(min_elements_to_replace(4, [1, 1, 1, 1]))