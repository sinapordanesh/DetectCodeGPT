def min_sum_last_two_cards(N, cards):
    while len(cards) > 2:
        min_sum = float('inf')
        min_index = -1
        for i in range(len(cards) - 2):
            current_sum = cards[i] + cards[i + 1] + cards[i + 2]
            if current_sum < min_sum:
                min_sum = current_sum
                min_index = i
        cards[min_index] += cards[min_index + 1] + cards[min_index + 2]
        cards.pop(min_index + 2)
        cards.pop(min_index + 1)
    
    return sum(cards)

# Sample Input 1
print(min_sum_last_two_cards(4, [3, 1, 4, 2]))

# Sample Input 2
print(min_sum_last_two_cards(6, [5, 2, 4, 1, 6, 9]))

# Sample Input 3
print(min_sum_last_two_cards(10, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))