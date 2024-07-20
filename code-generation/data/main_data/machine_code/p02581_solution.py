def max_points(N, cards):
    cards.sort()
    return min(cards[:N], cards[2*N:3*N]).count(cards[N])

N = 2
cards = [1, 2, 1, 2, 2, 1]
print(max_points(N, cards))

N = 3
cards = [1, 1, 2, 2, 3, 3, 3, 2, 1]
print(max_points(N, cards))

N = 3
cards = [1, 1, 2, 2, 2, 3, 3, 3, 1]
print(max_points(N, cards))