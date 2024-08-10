def one_card_poker(A, B):
    if A == B:
        return "Draw"
    elif A == 1:
        return "Bob"
    elif B == 1:
        return "Alice"
    elif A > B:
        return "Alice"
    else:
        return "Bob"