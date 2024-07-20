def consecutive_ones(grid):
    max_consecutive_ones = 0
    for row in grid:
        consecutive_ones = 0
        for num in row:
            if num == '1':
                consecutive_ones += 1
                max_consecutive_ones = max(max_consecutive_ones, consecutive_ones)
            else:
                consecutive_ones = 0
    return max_consecutive_ones

while True:
    n = int(input())
    if n == 0:
        break
    grid = [input() for _ in range(n)]
    print(consecutive_ones(grid))