def tag_game(A, V, B, W, T):
    if abs(A - B) <= (V - W) * T:
        return "YES"
    else:
        return "NO"