def count_subrectangles(H, W, N, cells):
    count = [0] * 10
    for i in range(N):
        row, col = cells[i]
        for r in range(max(1, row - 2), min(H, row + 1)):
            for c in range(max(1, col - 2), min(W, col + 1)):
                count[(min(3, row - r + 1) * min(3, col - c + 1)) - 1] += 1
    for c in count:
        print(c)

# Sample Input 1
count_subrectangles(4, 5, 8, [(1, 1), (1, 4), (1, 5), (2, 3), (3, 1), (3, 2), (3, 4), (4, 4)])

# Sample Input 2
count_subrectangles(10, 10, 20, [(1, 1), (1, 4), (1, 9), (2, 5), (3, 10), (4, 2), (4, 7), (5, 9), (6, 4), (6, 6), (6, 7), (7, 1), (7, 3), (7, 7), (8, 1), (8, 5), (8, 10), (9, 2), (10, 4), (10, 9)])

# Sample Input 3
# count_subrectangles(1000000000, 1000000000, 0, [])