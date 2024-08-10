def queens_case():
    while True:
        W, H = map(int, input().split())
        if W == 0 and H == 0:
            break
        palace = [input() for _ in range(H)]

        def next_moves(x, y):
            moves = []
            if x > 0:
                moves.append((x - 1, y))
            if x < W - 1:
                moves.append((x + 1, y))
            if y > 0:
                moves.append((x, y - 1))
            if y < H - 1:
                moves.append((x, y + 1))
            return moves

        queen_pos = [(x, y) for y in range(H) for x in range(W) if palace[y][x] == 'Q'][0]
        army_pos = [(x, y) for y in range(H) for x in range(W) if palace[y][x] == 'A'][0]
        exit_pos = [(x, y) for y in range(H) for x in range(W) if palace[y][x] == 'E']

        queen_moves = next_moves(*queen_pos)
        army_moves = next_moves(*army_pos)

        queen_can_escape = False
        army_can_catch = False

        for exit_cell in exit_pos:
            if queen_pos == exit_cell:
                queen_can_escape = True
                break

        while not queen_can_escape and not army_can_catch:
            for q_move in queen_moves:
                for a_move in army_moves:
                    if q_move == a_move:
                        army_can_catch = True
                        break
                    if q_move in exit_pos:
                        queen_can_escape = True
                        break
                if queen_can_escape or army_can_catch:
                    break

        if queen_can_escape:
            print("Queen can escape.")
        elif army_can_catch:
            print("Army can catch Queen.")
        else:
            print("Queen can not escape and Army can not catch Queen.")

queens_case()