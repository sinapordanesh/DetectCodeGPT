def max_time_gap(N, D):
    max_time_gap = 0
    for i in range(N+1):
        for j in range(i+1, N+1):
            time_gap = min(abs(D[i] - D[j]), 24 - abs(D[i] - D[j]))
            max_time_gap = max(max_time_gap, time_gap)
    return max_time_gap

# Use the function
print(max_time_gap(3, [7, 12, 8]))
print(max_time_gap(2, [11, 11]))
print(max_time_gap(1, [0]))