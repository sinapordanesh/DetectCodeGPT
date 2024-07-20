def min_absolute_difference(N, weights):
    min_diff = float('inf')
    for T in range(1, N):
        S1 = sum(weights[:T])
        S2 = sum(weights[T:])
        diff = abs(S1 - S2)
        min_diff = min(min_diff, diff)
    return min_diff

# Sample Input 1
print(min_absolute_difference(3, [1, 2, 3]))

# Sample Input 2
print(min_absolute_difference(4, [1, 3, 1, 1]))

# Sample Input 3
print(min_absolute_difference(8, [27, 23, 76, 2, 3, 5, 62, 52]))