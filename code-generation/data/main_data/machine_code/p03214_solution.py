def generate_thumbnail(N, frames):
    avg = sum(frames) / N
    min_diff = float('inf')
    index = 0
    
    for i in range(N):
        diff = abs(frames[i] - avg)
        if diff < min_diff:
            min_diff = diff
            index = i
    
    return index

# Test cases
print(generate_thumbnail(3, [1, 2, 3])) # 1
print(generate_thumbnail(4, [2, 5, 2, 5])) # 0