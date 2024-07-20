def riffle_shuffle(n, r, operations):
    cards = list(range(n))
    for op in operations:
        deck_a = cards[:n//2+1] if n%2 != 0 else cards[:n//2]
        deck_b = cards[n//2+1:] if n%2 != 0 else cards[n//2:]
        deck_c = []
        
        while len(deck_a) > 0 and len(deck_b) > 0:
            for _ in range(op):
                if len(deck_a) > 0:
                    deck_c.append(deck_a.pop())
                if len(deck_b) > 0:
                    deck_c.append(deck_b.pop())
        
        if len(deck_a) > 0:
            deck_c.extend(deck_a[::-1])
        if len(deck_b) > 0:
            deck_c.extend(deck_b[::-1])
        
        cards = deck_c
    
    return cards[-1]