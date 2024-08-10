def can_make_grid_symmetric(H, W, grid):
    def is_symmetric(grid):
        for i in range(H):
            for j in range(W):
                if grid[i][j] != grid[H-1-i][W-1-j]:
                    return False
        return True

    for i in range(H):
        for j in range(i+1, H):
            if grid[i] == grid[j]:
                continue
            if is_symmetric(grid):
                return "YES"
            for k in range(W):
                if grid[i][k] != grid[j][k]:
                    break
            else:
                return "NO"
            for k in range(H):
                grid[k][i], grid[k][j] = grid[k][j], grid[k][i]
            if is_symmetric(grid):
                return "YES"
            for k in range(H):
                grid[k][i], grid[k][j] = grid[k][j], grid[k][i]
    return "NO"

# Sample Input 1
print(can_make_grid_symmetric(2, 3, ['arc', 'rac']))

# Sample Input 2
print(can_make_grid_symmetric(3, 7, ['atcoder', 'regular', 'contest']))

# Sample Input 3
print(can_make_grid_symmetric(12, 12, ['bimonigaloaf', 'faurwlkbleht', 'dexwimqxzxbb', 'lxdgyoifcxid', 'ydxiliocfdgx', 'nfoabgilamoi', 'ibxbdqmzxxwe', 'pqirylfrcrnf', 'wtehfkllbura', 'yfrnpflcrirq', 'wvcclwgiubrk', 'lkbrwgwuiccv']))