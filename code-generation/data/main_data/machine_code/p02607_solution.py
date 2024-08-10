def count_odd_squares(N, arr):
    count = 0
    for i in range(N):
        if i % 2 == 1 and arr[i] % 2 == 1:
            count += 1
    return count

# Sample Input 1
print(count_odd_squares(5, [1, 3, 4, 5, 7]))

# Sample Input 2
print(count_odd_squares(15, [13, 76, 46, 15, 50, 98, 93, 77, 31, 43, 84, 90, 6, 24, 14]))