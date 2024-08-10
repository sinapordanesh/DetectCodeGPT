def card_game(n, cards):
    taro_score = 0
    hanako_score = 0
    
    for card in cards:
        if card[0] > card[1]:
            taro_score += 3
        elif card[0] < card[1]:
            hanako_score += 3
        else:
            taro_score += 1
            hanako_score += 1
    
    return str(taro_score) + " " + str(hanako_score)

n = 3
cards = [("cat", "dog"), ("fish", "fish"), ("lion", "tiger")]
print(card_game(n, cards))