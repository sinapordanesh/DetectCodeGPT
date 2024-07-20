def game_winner(X, Y):
    while X >= 2 or Y >= 2:
        if X >= 2:
            X, Y = X - 2, Y + 1
        else:
            Y, X = Y - 2, X + 1
    return "Alice" if X > Y else "Brown" 

X, Y = map(int, input().split())
print(game_winner(X, Y))