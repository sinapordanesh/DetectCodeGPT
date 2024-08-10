def min_operations(n, a):
    count = 0
    total_sum = 0
    for i in range(n):
        total_sum += a[i]
        if i % 2 == 0 and total_sum <= 0:
            count += abs(total_sum) + 1
            total_sum = 1
        elif i % 2 == 1 and total_sum >= 0:
            count += abs(total_sum) + 1
            total_sum = -1
    return count

# Sample Input 1
print(min_operations(4, [1, -3, 1, 0]))

# Sample Input 2
print(min_operations(5, [3, -6, 4, -5, 7]))

# Sample Input 3
print(min_operations(6, [-1, 4, 3, 2, -5, 4]))