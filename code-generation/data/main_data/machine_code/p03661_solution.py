def min_card_difference(N, cards):
    cards.sort()
    x = sum(cards[:N//2])
    y = sum(cards[N//2:])
    
    return abs(x - y)