def min_attacks_to_vanish(N, H, katana):
    total_attacks = 0
    for i in range(N):
        a_i, b_i = katana[i]
        if b_i >= a_i:
            total_attacks += max((H + b_i - 1) // b_i, 1)
        else:
            total_attacks += max((H - (b_i - a_i) + b_i - 1) // b_i, 1)
    return total_attacks