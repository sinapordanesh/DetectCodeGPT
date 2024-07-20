def min_operations(N, p):
    count = 0
    for i in range(N):
        if p[i] == i+1:
            count += 1
    return (count + 1) // 2

# Sample Input 1
print(min_operations(5, [1, 4, 3, 5, 2]))

# Sample Input 2
print(min_operations(2, [1, 2]))

# Sample Input 3
print(min_operations(2, [2, 1]))

# Sample Input 4
print(min_operations(9, [1, 2, 4, 9, 5, 8, 7, 3, 6]))