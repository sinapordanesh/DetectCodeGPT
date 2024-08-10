def bishop_squares(H, W):
    return min(H, W) + max(H, W) - 1

# Test the function with the sample inputs
print(bishop_squares(4, 5))
print(bishop_squares(7, 3))
print(bishop_squares(1000000000, 1000000000))