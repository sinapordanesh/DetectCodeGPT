def shuffle_deck(deck, shuffles):
    for h in shuffles:
        deck = deck[-h:] + deck[:-h]
    return deck

data = input()
while data != "-":
    deck = data
    shuffles = []
    num_shuffles = int(input())
    for _ in range(num_shuffles):
        shuffles.append(int(input()))
    print(shuffle_deck(deck, shuffles))
    data = input()