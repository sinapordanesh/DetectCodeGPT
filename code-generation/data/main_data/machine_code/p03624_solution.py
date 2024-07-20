def smallest_letter_not_in_string(S):
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter not in S:
            return letter
    return "None"