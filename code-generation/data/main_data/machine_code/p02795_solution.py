def min_operations_needed(H, W, N):
    min_operations = min((N + i - 1) // i for i in range(1, max(H, W) + 1))
    return min_operations

# Sample Input 1
print(min_operations_needed(3, 7, 10))

# Sample Input 2
print(min_operations_needed(14, 12, 112))

# Sample Input 3
print(min_operations_needed(2, 100, 200))