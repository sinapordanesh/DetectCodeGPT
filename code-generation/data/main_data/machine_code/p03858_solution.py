def count_pairs_of_pinholes(N, a, b, pinholes):
    count = 0
    for i in range(1, N+1):
        if i == a or i == b:
            continue
        if abs(pinholes[a-1][0] - pinholes[i-1][0]) + abs(pinholes[a-1][1] - pinholes[i-1][1]) == abs(pinholes[b-1][0] - pinholes[i-1][0]) + abs(pinholes[b-1][1] - pinholes[i-1][1]):
            count += 1
    return count

# Sample Input 1
print(count_pairs_of_pinholes(5, 1, 2, [[1, 1], [4, 3], [6, 1], [5, 5], [4, 8]]))

# Sample Input 2
print(count_pairs_of_pinholes(6, 2, 3, [[1, 3], [5, 3], [3, 5], [8, 4], [4, 7], [2, 5]]))

# Sample Input 3
print(count_pairs_of_pinholes(8, 1, 2, [[1, 5], [4, 3], [8, 2], [4, 7], [8, 8], [3, 3], [6, 6], [4, 8]]))