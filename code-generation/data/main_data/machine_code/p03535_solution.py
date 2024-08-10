def max_time_gap(N, D):
    max_gap = 0
    for i in range(N):
        for j in range(i+1, N+1):
            gap = min(abs(D[i] - D[j]), 24 - abs(D[i] - D[j]))
            max_gap = max(max_gap, gap)
    
    return max_gap

# Test the function
print(max_time_gap(3, [7, 12, 8])) # 4
print(max_time_gap(2, [11, 11])) # 2
print(max_time_gap(1, [0])) # 0