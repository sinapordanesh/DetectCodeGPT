def min_recolor_stones(N, S):
    count = 0
    for i in range(1, N):
        if S[i] == '.' and S[i-1] == '#':
            count += 1
    return count

# Sample Input 1
print(min_recolor_stones(3, "#.#"))

# Sample Input 2
print(min_recolor_stones(5, "#.##."))

# Sample Input 3
print(min_recolor_stones(9, "........."))