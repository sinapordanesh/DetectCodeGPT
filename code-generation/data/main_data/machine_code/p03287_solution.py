def box_pairs(N, M, A):
    count = 0
    prefix_sum = [0] * (N + 1)
    remainder_count = [0] * M
    prefix_sum[0] = 0
    for i in range(1, N + 1):
        prefix_sum[i] = (prefix_sum[i - 1] + A[i - 1]) % M
    for i in range(N + 1):
        remainder_count[prefix_sum[i]] += 1
    for i in range(M):
        count += remainder_count[i] * (remainder_count[i] - 1) // 2
    return count

# Sample Input 1
print(box_pairs(3, 2, [4, 1, 5]))

# Sample Input 2
print(box_pairs(13, 17, [29, 7, 5, 7, 9, 51, 7, 13, 8, 55, 42, 9, 81]))

# Sample Input 3
print(box_pairs(10, 400000000, [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]))