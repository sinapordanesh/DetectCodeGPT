def min_operations(N, a, b):
    x = 0
    for num in a:
        x ^= num
    
    y = 0
    for num in b:
        y ^= num
    
    if x != y:
        return -1
    
    count = 0
    for i in range(N):
        if a[i] != b[i]:
            count += 1
    
    return count

# Sample Input 1
print(min_operations(3, [0, 1, 2], [3, 1, 0])) # 2

# Sample Input 2
print(min_operations(3, [0, 1, 2], [0, 1, 2])) # 0

# Sample Input 3
print(min_operations(2, [1, 1], [0, 0])) # -1

# Sample Input 4
print(min_operations(4, [0, 1, 2, 3], [1, 0, 3, 2])) # 5