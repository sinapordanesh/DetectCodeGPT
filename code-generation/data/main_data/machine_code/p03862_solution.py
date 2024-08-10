def min_operations(N, x, candies):
    operations = 0
    for i in range(N-1):
        if candies[i] + candies[i+1] > x:
            diff = candies[i] + candies[i+1] - x
            operations += diff
            candies[i+1] = max(0, candies[i+1] - diff)
    return operations

# Sample Input 1
print(min_operations(3, 3, [2, 2, 2]))

# Sample Input 2
print(min_operations(6, 1, [1, 6, 1, 2, 0, 4]))

# Sample Input 3
print(min_operations(5, 9, [3, 1, 4, 1, 5]))

# Sample Input 4
print(min_operations(2, 0, [5, 5]))