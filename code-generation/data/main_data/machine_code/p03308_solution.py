def max_absolute_difference(N, A):
    max_diff = 0
    for i in range(N):
        for j in range(i+1, N):
            diff = abs(A[i] - A[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff

# Sample Input 1
print(max_absolute_difference(4, [1, 4, 6, 3]))

# Sample Input 2
print(max_absolute_difference(2, [1000000000, 1]))

# Sample Input 3
print(max_absolute_difference(5, [1, 1, 1, 1, 1]))