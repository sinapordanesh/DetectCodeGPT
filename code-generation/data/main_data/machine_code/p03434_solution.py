def optimal_score(N, cards):
    cards.sort(reverse=True)
    alice = 0
    bob = 0
    for i in range(N):
        if i % 2 == 0:
            alice += cards[i]
        else:
            bob += cards[i]
    return alice - bob

# Input
N = 4
cards = [20, 18, 2, 18]

# Output
print(optimal_score(N, cards))