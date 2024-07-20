def num_attacks_to_win(H, A):
    if H % A == 0:
        return H // A
    else:
        return H // A + 1