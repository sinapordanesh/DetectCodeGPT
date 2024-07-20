def rolling_dice(h, w, grid, start_row, start_col, dest_row, dest_col):
    penalty = 0
    while start_row != dest_row or start_col != dest_col:
        if start_row < dest_row:
            penalty += grid[start_row][start_col] * 2
            start_row += 1
        elif start_row > dest_row:
            penalty += grid[start_row][start_col] * 5
            start_row -= 1
        elif start_col < dest_col:
            penalty += grid[start_row][start_col] * 3
            start_col += 1
        else:
            penalty += grid[start_row][start_col] * 4
            start_col -= 1
    return penalty

print(rolling_dice(1, 2, [[8, 8]], 0, 0, 0, 1))
print(rolling_dice(3, 3, [[1, 2, 5], [2, 8, 3], [0, 1, 2]], 0, 0, 2, 2))
print(rolling_dice(1, 2, [[1, 2]], 0, 0, 0, 1))
print(rolling_dice(3, 4, [[1, 2, 3], [4, 5, 6]], 0, 0, 1, 2))