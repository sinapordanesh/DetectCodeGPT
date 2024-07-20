def make_sequence(input_data):
    for line in input_data:
        n, m, p = map(int, line.split())
        if n == 0 and m == 0 and p == 0:
            break
        moves = [list(map(int, input().split())) for _ in range(p)]
        board = [[['.'] * n for _ in range(n)] for _ in range(n)]
        players = ['Black', 'White']
        current_player = 0
        winner = None
        for i, (x, y) in enumerate(moves):
            z = 0
            while z < n and board[x-1][y-1][z] != '.':
                z += 1
            board[x-1][y-1][z] = players[current_player]
            directions = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)]
            for dx, dy, dz in directions:
                count = 1
                for j in range(1, m):
                    if 0 <= x-1+j*dx < n and 0 <= y-1+j*dy < n and 0 <= z-1+j*dz < n:
                        if board[x-1+j*dx][y-1+j*dy][z-1+j*dz] == players[current_player]:
                            count += 1
                        else:
                            break
                if count == m:
                    winner = players[current_player]
                    break
            if winner is not None:
                break
            current_player = 1 - current_player
        if winner is None:
            print('Draw')
        else:
            print(f'{winner} {i+1}')