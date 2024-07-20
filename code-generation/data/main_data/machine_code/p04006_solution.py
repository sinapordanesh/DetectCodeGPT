def min_time_to_have_all_colors(N, x, a):
    total_time = sum(a)
    min_time = min(a)
    return total_time + (N-1)*x - min_time

# Sample Input 1
# N = 2, x = 10, a = [1, 100]
# Sample Output 1
# Result: 12
print(min_time_to_have_all_colors(2, 10, [1, 100]))

# Sample Input 2
# N = 3, x = 10, a = [100, 1, 100]
# Sample Output 2
# Result: 23
print(min_time_to_have_all_colors(3, 10, [100, 1, 100]))

# Sample Input 3
# N = 4, x = 10, a = [1, 2, 3, 4]
# Sample Output 3
# Result: 10
print(min_time_to_have_all_colors(4, 10, [1, 2, 3, 4]))