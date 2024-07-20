def minimal_backgammon(N, T, L, B, lose_squares, back_squares):
    def calculate_probability(current_square, remaining_turns):
        if current_square == N:
            return 1.0
        if remaining_turns == 0:
            return 0.0
        
        total_probability = 0
        for dice_roll in range(1, 7):
            next_square = min(current_square + dice_roll, N)
            if next_square in lose_squares:
                total_probability += calculate_probability(current_square, remaining_turns - 1)
            elif next_square in back_squares:
                total_probability += calculate_probability(0, remaining_turns - 1)
            else:
                total_probability += calculate_probability(next_square, remaining_turns - 1)
        
        return total_probability / 6.0
    
    return calculate_probability(0, T)

# Sample Input
print(minimal_backgammon(6, 1, 0, 0, [], []))
print(minimal_backgammon(7, 1, 0, 0, [], []))
print(minimal_backgammon(7, 2, 0, 0, [], []))
print(minimal_backgammon(6, 6, 1, 1, [2], [5, 6]))