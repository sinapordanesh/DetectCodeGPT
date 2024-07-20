def count_good_boards(N, board):
    count = 0
    for A in range(N):
        for B in range(N):
            good_board = True
            for i in range(N):
                for j in range(N):
                    if board[i][j] != board[(i+A)%N][(j+B)%N]:
                        good_board = False
                        break
                if not good_board:
                    break
            if good_board:
                count += 1
    return count

# Sample Input 1
print(count_good_boards(2, ['ab', 'ca']))

# Sample Input 2
print(count_good_boards(4, ['aaaa', 'aaaa', 'aaaa', 'aaaa']))

# Sample Input 3
print(count_good_boards(5, ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy']))