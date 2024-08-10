def max_moves(N, heights):
    max_moves = 0
    current_moves = 0
    for i in range(N - 1):
        if heights[i] >= heights[i + 1]:
            current_moves += 1
        else:
            max_moves = max(max_moves, current_moves)
            current_moves = 0
    return max_moves

# Sample Input 1
print(max_moves(5, [10, 4, 8, 7, 3]))

# Sample Input 2
print(max_moves(7, [4, 4, 5, 6, 6, 5, 5]))

# Sample Input 3
print(max_moves(4, [1, 2, 3, 4]))