def count_black_subrectangles(H, W, N, cells):
    count = [0] * 10
    
    for cell in cells:
        row, col = cell
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 1 <= row + i <= H - 2 and 1 <= col + j <= W - 2:
                    black_count = 0
                    for k in range(3):
                        for l in range(3):
                            if (row + i + k, col + j + l) in cells:
                                black_count += 1
                    count[black_count] += 1
    
    return count

# Sample Input 1
H, W, N = 4, 5, 8
cells = [(1, 1), (1, 4), (1, 5), (2, 3), (3, 1), (3, 2), (3, 4), (4, 4)]
output1 = count_black_subrectangles(H, W, N, cells)

# Sample Input 2
H, W, N = 10, 10, 20
cells = [(1, 1), (1, 4), (1, 9), (2, 5), (3, 10), (4, 2), (4, 7), (5, 9), (6, 4), (6, 6), (6, 7), (7, 1), (7, 3), (7, 7), (8, 1), (8, 5), (8, 10), (9, 2), (10, 4), (10, 9)]
output2 = count_black_subrectangles(H, W, N, cells)