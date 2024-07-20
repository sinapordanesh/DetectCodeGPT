def stone_game(X, Y):
    if X == Y == 0:
        return "Brown"
    elif Y == 0:
        return "Alice"
    elif X == 1 and Y == 1:
        return "Alice"
    elif X <= 2:
        return "Brown"
    elif Y <= 2:
        return "Alice"
    elif X % 2 == 0 and Y % 2 == 0:
        return "Alice"
    else:
        return "Alice" if abs(X - Y) <= 2 else "Brown"

X, Y = map(int, input().split())
print(stone_game(X, Y))