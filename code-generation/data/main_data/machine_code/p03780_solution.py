def unnecessary_cards(N, K, cards):
    count = 0
    for i in range(N):
        if sum(cards) - cards[i] < K:
            count += 1
    return count

#Sample Input 1
print(unnecessary_cards(3, 6, [1, 4, 3]))

#Sample Input 2
print(unnecessary_cards(5, 400, [3, 1, 4, 1, 5]))

#Sample Input 3
print(unnecessary_cards(6, 20, [10, 4, 3, 10, 25, 2]))