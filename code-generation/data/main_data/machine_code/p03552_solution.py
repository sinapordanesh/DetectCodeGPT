def max_score(N, Z, W, cards):
    X = max(Z, W)
    Y = min(Z, W)
    
    if N == 1:
        score = abs(X - cards[0])
    else:
        score = abs(cards[-1] - cards[-2])
    
    return score

# Sample Input 1
print(max_score(3, 100, 100, [10, 1000, 100]))

# Sample Input 2
print(max_score(3, 100, 1000, [10, 100, 100]))

# Sample Input 3
print(max_score(5, 1, 1, [1, 1, 1, 1, 1]))

# Sample Input 4
print(max_score(1, 1, 1, [1000000000]))