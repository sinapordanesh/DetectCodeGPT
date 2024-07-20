def min_difference(N, cards):
    cards.sort()
    Snuke = sum(cards[:N-1])
    Raccoon = cards[N-1]
    return abs(Snuke - Raccoon)