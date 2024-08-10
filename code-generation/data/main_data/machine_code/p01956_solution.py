def window_area(N, H, W, instructions):
    total_area = 0
    for i in range(N):
        if i % 2 == 0:
            total_area += H * (W - instructions[i])
        else:
            total_area += H * instructions[i]
    return total_area

# Sample Input 1
print(window_area(4, 3, 3, [1, 1, 2, 3]))

# Sample Input 2
print(window_area(8, 10, 18, [2, 12, 16, 14, 18, 4, 17, 16]))

# Sample Input 3
print(window_area(6, 2, 2, [0, 2, 2, 2, 2, 0]))

# Sample Input 4
print(window_area(4, 1, 4, [3, 3, 2, 2]))

# Sample Input 5
print(window_area(8, 7, 15, [5, 0, 9, 14, 0, 4, 4, 15]))