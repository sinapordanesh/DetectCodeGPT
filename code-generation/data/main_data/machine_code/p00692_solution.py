def minimal_penalty(card_layouts):
    penalties = []
    
    for layout in card_layouts:
        cards = layout.split()
        cards = list(map(int, cards))
        
        penalty = 0
        while True:
            found_pair = False
            for i in range(len(cards) - 1):
                if cards[i] == cards[i + 1]:
                    found_pair = True
                    cards = cards[:i] + cards[i + 2:]
                    penalty += 2
                    break
            if not found_pair:
                break
        
        if len(cards) > 0:
            penalty += len(cards)
            
        penalties.append(penalty)
    
    return penalties

# Sample Input
card_layouts = [
    "1 4 5 2",
    "3 1 4 3",
    "5 4 2 2",
    "4 5 2 3",
    "1 1 3 5",
    "5 1 5 1",
    "4 5 3 2",
    "3 2 1 4",
    "1 4 5 3",
    "2 3 4 2",
    "1 2 1 2",
    "5 4 5 4",
    "2 1 2 1",
    "3 5 3 4",
    "3 3 5 4",
    "4 2 3 1",
    "2 5 3 1",
    "3 5 4 2",
    "1 5 4 1",
    "4 5 3 2"
]

# Calling the function
result = minimal_penalty(card_layouts)
for res in result:
    print(res)