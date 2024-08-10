def minimum_sadness(N, A):
    total = sum(A)
    min_sadness = float('inf')
    for i in range(N):
        b = (total - sum(abs(A[j] - (i+1+j)) for j in range(N)))
        min_sadness = min(min_sadness, b)
    return min_sadness

# Sample Input
print(minimum_sadness(5, [2, 2, 3, 5, 5])) # Output: 2
print(minimum_sadness(9, [1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: 0
print(minimum_sadness(6, [6, 5, 4, 3, 2, 1])) # Output: 18
print(minimum_sadness(7, [1, 1, 1, 1, 2, 3, 4])) # Output: 6