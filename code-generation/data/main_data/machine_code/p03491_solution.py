def determine_winner(N, L, strings):
    if L == 1:
        return "Bob"
    
    if N % 2 == 0:
        return "Bob"
    else:
        return "Alice"