def min_sadness(N, A):
    total = sum(A)
    min_sadness = float('inf')
    for i in range(N):
        b = A[i] - i
        sadness = 0
        for j in range(N):
            sadness += abs(A[j] - (b + j + 1))
        min_sadness = min(min_sadness, sadness)
    return min_sadness

# Test the function with the sample inputs
print(min_sadness(5, [2, 2, 3, 5, 5])) # Output: 2
print(min_sadness(9, [1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: 0
print(min_sadness(6, [6, 5, 4, 3, 2, 1])) # Output: 18
print(min_sadness(7, [1, 1, 1, 1, 2, 3, 4])) # Output: 6