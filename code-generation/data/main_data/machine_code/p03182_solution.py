def max_possible_score(N, M, queries):
    score = 0
    ones = [0] * (N + 1)
    
    for l, r, a in queries:
        ones[l] += a
        ones[r + 1] -= a
    
    for i in range(1, N + 1):
        ones[i] += ones[i - 1]
    
    for i in range(1, N + 1):
        score = max(score, score + ones[i])
    
    return score

# Sample Input 1
print(max_possible_score(5, 3, [(1, 3, 10), (2, 4, -10), (3, 5, 10)]))

# Sample Input 2
print(max_possible_score(3, 4, [(1, 3, 100), (1, 1, -10), (2, 2, -20), (3, 3, -30)]))

# Sample Input 3
print(max_possible_score(1, 1, [(1, 1, -10)]))

# Sample Input 4
print(max_possible_score(1, 5, [(1, 1, 1000000000), (1, 1, 1000000000), (1, 1, 1000000000), (1, 1, 1000000000), (1, 1, 1000000000)]))

# Sample Input 5
print(max_possible_score(6, 8, [(5, 5, 3), (1, 1, 10), (1, 6, -8), (3, 6, 5), (3, 4, 9), (5, 5, -2), (1, 3, -6), (4, 6, -7)]))