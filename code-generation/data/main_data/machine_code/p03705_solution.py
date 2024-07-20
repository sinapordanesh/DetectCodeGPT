def possible_sums(N, A, B):
    min_sum = A * N + (N - 1) * N // 2
    max_sum = B * N - (N - 1) * N // 2
    diff = max_sum - min_sum + 1
    if diff <= 0:
        return 0
    return diff

# Test the function
print(possible_sums(4, 4, 6))
print(possible_sums(5, 4, 3))
print(possible_sums(1, 7, 10))
print(possible_sums(1, 3, 3))