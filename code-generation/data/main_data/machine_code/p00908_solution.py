def sliding_block_puzzle(H, W, initial_placement):
    def move_king(king_pos, open_squares):
        for square in open_squares:
            if king_pos[0][0] == square or king_pos[1][0] == square:
                return 1
            if king_pos[0][1] == square or king_pos[1][1] == square:
                return 1
        return -1

    def bfs(king_pos, pawn_pos, open_squares, obstacles):
        queue = [(king_pos, pawn_pos, 0)]
        visited = set()
        while queue:
            k, p, moves = queue.pop(0)
            if k == [(0, 0), (0, 1)]:
                return moves
            if (k, p) in visited:
                continue
            visited.add((k, p))
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_king = [(k[0][0] + dx, k[0][1] + dy), (k[1][0] + dx, k[1][1] + dy)]
                if all(0 <= x < H and 0 <= y < W and (x, y) not in obstacles for x, y in new_king):
                    new_pawn = [(x + dx, y + dy) for x, y in p]
                    if all(0 <= x < H and 0 <= y < W and (x, y) not in obstacles for x, y in new_pawn) and all(
                            x in open_squares for x in new_pawn):
                        queue.append((new_king, new_pawn, moves + 1))
        return -1

    king_pos = []
    pawn_pos = []
    open_squares = []
    obstacles = []
    for i in range(H):
        for j in range(W):
            if initial_placement[i][j] == 'X':
                king_pos.append((i, j))
            elif initial_placement[i][j] == 'o':
                pawn_pos.append((i, j))
            elif initial_placement[i][j] == '.':
                open_squares.append((i, j))
            elif initial_placement[i][j] == '*':
                obstacles.append((i, j))

    return bfs(king_pos, pawn_pos, open_squares, obstacles) if move_king(king_pos, open_squares) == 1 else -1
