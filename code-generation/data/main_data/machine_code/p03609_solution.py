def remaining_sand(X, t):
    return max(X - t, 0) if X >= t else 0