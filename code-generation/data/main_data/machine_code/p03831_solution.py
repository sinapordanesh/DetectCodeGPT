def min_fatigue_level(N, A, B, X):
    total_fatigue = 0
    
    for i in range(N-1):
        walk_distance = X[i+1] - X[i]
        walk_fatigue = walk_distance * A
        total_fatigue += min(walk_fatigue, B)
    
    return total_fatigue