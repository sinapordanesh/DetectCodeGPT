def max_remaining_cards(N, cards):
    cards.sort()
    unique_cards = set(cards)
    return min(len(unique_cards), (N + 1) // 2)

# Sample Input 1
print(max_remaining_cards(5, [1, 2, 1, 3, 7]))

# Sample Input 2
print(max_remaining_cards(15, [1, 3, 5, 2, 1, 3, 2, 8, 8, 6, 2, 6, 11, 1, 1]))