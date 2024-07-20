def min_presses(n, m, a):
    total_presses = 0
    for i in range(n-1):
        total_presses += (a[i] - a[i+1] + m) % m
    return total_presses

# Sample Input 1
print(min_presses(4, 6, [1, 5, 1, 4]))

# Sample Input 2
print(min_presses(10, 10, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))