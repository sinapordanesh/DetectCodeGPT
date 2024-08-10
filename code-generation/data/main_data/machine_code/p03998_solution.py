def card_game_winner(S_A, S_B, S_C):
    players = {'A': list(S_A), 'B': list(S_B), 'C': list(S_C)}
    current_player = 'A'
    
    while True:
        if not players[current_player]:
            return current_player
        
        card = players[current_player].pop(0)
        current_player = card

# Sample Input
print(card_game_winner("aca", "accc", "ca"))
print(card_game_winner("abcb", "aacb", "bccc"))