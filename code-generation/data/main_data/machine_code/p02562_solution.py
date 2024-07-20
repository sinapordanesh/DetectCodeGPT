def max_sum_chosen_squares(N, K, grid):
    def backtrack(row, chosen, curr_sum):
        nonlocal max_sum
        if row == N:
            if curr_sum > max_sum:
                max_sum = curr_sum
                for i in range(N):
                    for j in range(N):
                        if (i, j) in chosen:
                            result[i][j] = 'X'
                        else:
                            result[i][j] = '.'
            return
        for i in range(N):
            if i in chosen:
                continue
            new_chosen = chosen.copy()
            new_chosen.add(i)
            new_sum = curr_sum + grid[row][i]
            valid = True
            for j in range(row):
                if abs(i - j) <= 1 and j in chosen:
                    valid = False
                    break
            if valid:
                backtrack(row + 1, new_chosen, new_sum)

    max_sum = 0
    result = [['.'] * N for _ in range(N)]
    backtrack(0, set(), 0)
    
    print(max_sum)
    for i in range(N):
        print(''.join(result[i]))