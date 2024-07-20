def game_winner(N, A, B):
    if (B - A) % 2 == 0:
        return "Alice"
    else:
        return "Borys"