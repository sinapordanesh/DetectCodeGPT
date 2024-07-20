def min_moves(N, M, coordinates):
    coordinates.sort()
    current_pos = 0
    moves = 0
    
    for i in range(M):
        target_pos = coordinates[i]
        moves += abs(target_pos - current_pos)
        current_pos = target_pos
    
    return moves

# Sample Input 1
print(min_moves(2, 5, [10, 12, 1, 2, 14]))

# Sample Input 2
print(min_moves(3, 7, [-10, -3, 0, 9, -100, 2, 17]))

# Sample Input 3
print(min_moves(100, 1, [-100000]))