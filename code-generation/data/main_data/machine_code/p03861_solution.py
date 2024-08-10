def count_divisible_nums(a, b, x):
    count = 0
    for i in range(a, b+1):
        if i % x == 0:
            count += 1
    return count

# Sample Input 1
print(count_divisible_nums(4, 8, 2))

# Sample Input 2
print(count_divisible_nums(0, 5, 1))

# Sample Input 3
print(count_divisible_nums(9, 9, 2))

# Sample Input 4
print(count_divisible_nums(1, 1000000000000000000, 3))