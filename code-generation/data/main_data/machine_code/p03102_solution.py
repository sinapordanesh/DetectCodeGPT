def correctly_solved_codes(N, M, C, B, codes):
    count = 0
    for i in range(N):
        total = sum([codes[i][j] * B[j] for j in range(M)]) + C
        if total > 0:
            count += 1
    return count

# Sample Input 1
print(correctly_solved_codes(2, 3, -10, [1, 2, 3], [[3, 2, 1], [1, 2, 2]]))

# Sample Input 2
print(correctly_solved_codes(5, 2, -4, [-2, 5], [[100, 41], [100, 40], [-3, 0], [-6, -2], [18, -13]]))

# Sample Input 3
print(correctly_solved_codes(3, 3, 0, [100, -100, 0], [[0, 100, 100], [100, 100, 100], [-100, 100, 100]]))