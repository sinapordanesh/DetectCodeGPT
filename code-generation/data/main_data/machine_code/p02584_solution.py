def min_dest_coordinate(X, K, D):
    X = abs(X)
    max_move = min(K, X // D)
    
    K -= max_move
    X -= max_move * D
    
    if K % 2 == 0:
        return X
    else:
        return abs(X - D)

# Sample Input 1
print(min_dest_coordinate(6, 2, 4))

# Sample Input 2
print(min_dest_coordinate(7, 4, 3))

# Sample Input 3
print(min_dest_coordinate(10, 1, 2))

# Sample Input 4
print(min_dest_coordinate(1000000000000000, 1000000000000000, 1000000000000000))