def min_walking_length(N, m, restrictions):
    shops = [i for i in range(N)]
    min_length = 0
    
    for i in range(1, N + 1):
        if i in restrictions:
            idx = restrictions.index(i)
            diff = abs(restrictions[idx] - restrictions[idx + 1])
            min_length += diff
    
    return min_length + N + 1 - len(restrictions) - 1 - len(set(restrictions))

# Test the function with the first sample input
print(min_walking_length(10, 3, [3, 7, 8, 9, 2, 5]))