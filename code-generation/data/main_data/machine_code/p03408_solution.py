def max_earn(N, blue_cards, M, red_cards):
    max_earn = 0
    for card in blue_cards:
        if card in red_cards:
            max_earn -= 1
        else:
            max_earn += 1
    return max_earn