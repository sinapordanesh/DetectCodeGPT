def min_spells_required(N, colors):
    count = 0
    for i in range(1, N-1):
        if colors[i] == colors[i-1]:
            colors[i] = 0
            count += 1
    return count

# Sample Input 1
print(min_spells_required(5, [1, 1, 2, 2, 2])) # 2

# Sample Input 2
print(min_spells_required(3, [1, 2, 1])) # 0

# Sample Input 3
print(min_spells_required(5, [1, 1, 1, 1, 1])) # 2

# Sample Input 4
print(min_spells_required(14, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 1, 2, 3, 4])) # 4