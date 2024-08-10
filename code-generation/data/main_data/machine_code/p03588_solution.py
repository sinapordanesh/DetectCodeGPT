def max_players(N, facts):
    facts.sort(reverse=True)
    max_players = facts[0][0] + facts[0][1]
    for i in range(1, N):
        if facts[i][1] < max_players:
            max_players = max_players + (facts[i][0] - facts[i][1])
    return max_players

# Sample Input 1
print(max_players(3, [(4, 7), (2, 9), (6, 2)]))

# Sample Input 2
print(max_players(5, [(1, 10), (3, 6), (5, 2), (4, 4), (2, 8)]))

# Sample Input 3
print(max_players(2, [(1, 1000000000), (1000000000, 1)]))