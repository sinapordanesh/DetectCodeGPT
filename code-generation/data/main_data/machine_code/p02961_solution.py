def golf_game(X, Y, K):
    def manhattan_distance(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)
    
    if (manhattan_distance(0, 0, X, Y) % 2 != K % 2) or (K < manhattan_distance(0, 0, X, Y)):
        return False
    
    return True