def find_contiguous_subsequences(N, A):
    count = 0
    prefix_sum = {0: 1}
    current_sum = 0
    for num in A:
        current_sum += num
        count += prefix_sum.get(current_sum, 0)
        prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
    return count