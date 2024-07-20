def hanafuda_shuffle(n, r, operations):
    deck = list(range(1, n+1))
    
    for op in operations:
        p, c = op
        top_cards = deck[p-1:p+c-1]
        deck = top_cards + deck[:p-1] + deck[p+c-1:]
    
    return deck[0]