def min_steps_to_solve_puzzle(puzzle):
    target = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ]
    steps = 0
    for i in range(4):
        for j in range(4):
            if puzzle[i][j] != target[i][j]:
                steps += 1
    return steps

# Sample Input
puzzle = [
    [1, 2, 3, 4],
    [6, 7, 8, 0],
    [5, 10, 11, 12],
    [9, 13, 14, 15]
]

print(min_steps_to_solve_puzzle(puzzle))