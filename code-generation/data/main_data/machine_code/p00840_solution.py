def widest_mobile(datasets):
    results = []
    for data in datasets:
        r, s, weights = data[0], data[1], data[2:]
        total_weight = sum(weights)
        
        def find_width(n, m, a, b):
            if n == 0 or m == 0:
                return a + b
            return a * find_width(n-1, m, a+1, b) / n + find_width(n, m-1, a, b+1) * b / m
        
        def find_widest_mobile(total_weight, width, stones):
            if total_weight == 0:
                return width if width < r else float('inf')
            if width >= r:
                return float('inf')
            
            max_width = float('inf')
            for i in range(len(stones)):
                new_stones = stones[:i] + stones[i+1:]
                new_width = find_width(stones[i], total_weight-stones[i], 1, 1)
                max_width = min(max_width, find_widest_mobile(total_weight-stones[i], width+new_width, new_stones))
            
            return max_width
        
        result = find_widest_mobile(total_weight, 0, weights)
        results.append(result if result != float('inf') else -1)
    
    return results

datasets = [
    [1.3, 3, 1, 2, 1],
    [1.4, 3, 1, 2, 1],
    [2.0, 3, 1, 2, 1],
    [1.59, 4, 2, 1, 1, 3],
    [1.7143, 4, 1, 2, 3, 5]
]

print(widest_mobile(datasets))