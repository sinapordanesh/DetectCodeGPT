def min_modifications(N, M, A, changes):
    # Initialize a dictionary to store the count of each number
    count = {}
    for num in A:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # Function to calculate the minimum number of modifications needed
    def min_mods(count):
        max_count = max(count.values())
        return N - max_count
    
    # Output list to store the results
    output = []
    
    # Calculate the minimum number of modifications after each change
    for i in range(M):
        x, y = changes[i]
        count[x] -= 1
        count[y] = count.get(y, 0) + 1
        output.append(min_mods(count))
    
    return output

# Sample Input 1
N1, M1 = 5, 3
A1 = [1, 1, 3, 4, 5]
changes1 = [(1, 2), (2, 5), (5, 4)]
print(min_modifications(N1, M1, A1, changes1))

# Sample Input 2
N2, M2 = 4, 4
A2 = [4, 4, 4, 4]
changes2 = [(4, 1), (3, 1), (1, 1), (2, 1)]
print(min_modifications(N2, M2, A2, changes2))

# Sample Input 3
N3, M3 = 10, 10
A3 = [8, 7, 2, 9, 10, 6, 6, 5, 5, 4]
changes3 = [(8, 1), (6, 3), (6, 2), (7, 10), (9, 7), (9, 9), (2, 4), (8, 1), (1, 8), (7, 7)]
print(min_modifications(N3, M3, A3, changes3))