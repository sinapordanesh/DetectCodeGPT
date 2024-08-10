def smallest_window(N, S, arr):
    min_len = float('inf')
    window_sum = 0
    start = 0

    for end in range(N):
        window_sum += arr[end]

        while window_sum >= S:
            min_len = min(min_len, end - start + 1)
            window_sum -= arr[start]
            start += 1

    return min_len if min_len != float('inf') else 0

# Sample Input
print(smallest_window(6, 4, [1, 2, 1, 2, 3, 2])) # 2
print(smallest_window(6, 6, [1, 2, 1, 2, 3, 2])) # 3
print(smallest_window(3, 7, [1, 2, 3])) # 0