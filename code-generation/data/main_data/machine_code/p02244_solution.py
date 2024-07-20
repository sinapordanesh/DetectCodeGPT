def print_board(k, positions):
    board = [['.' for _ in range(8)] for _ in range(8)]
    for r, c in positions:
        board[r][c] = 'Q'
    
    for row in board:
        print(''.join(row))

k = 2
positions = [(2, 2), (5, 3)]

print_board(k, positions)