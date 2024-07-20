def number_of_integers(N, P):
    count = 0
    min_seen = float('inf')
    for i in range(N):
        if P[i] <= min_seen:
            count += 1
        min_seen = min(min_seen, P[i])
    return count

# Sample Input 1
print(number_of_integers(5, [4, 2, 5, 1, 3]))

# Sample Input 2
print(number_of_integers(4, [4, 3, 2, 1]))

# Sample Input 3
print(number_of_integers(6, [1, 2, 3, 4, 5, 6]))

# Sample Input 4
print(number_of_integers(8, [5, 7, 4, 2, 6, 8, 1, 3]))

# Sample Input 5
print(number_of_integers(1, [1]))