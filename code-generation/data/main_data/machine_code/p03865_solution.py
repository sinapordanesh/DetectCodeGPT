def game_winner(s):
    if s[0] == s[-1]:
        return "Second"
    else:
        return "First"