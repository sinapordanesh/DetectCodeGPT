def game_score(N, Z, W, cards):
    if N == 1:
        return abs(cards[0] - W)
    else:
        return max(abs(cards[-1] - W), abs(cards[-2] - cards[-1]))  

# Sample Input 1
print(game_score(3, 100, 100, [10, 1000, 100]))

# Sample Input 2
print(game_score(3, 100, 1000, [10, 100, 100]))

# Sample Input 3
print(game_score(5, 1, 1, [1, 1, 1, 1, 1]))

# Sample Input 4
print(game_score(1, 1, 1, [1000000000]))