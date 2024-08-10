def fractal_distance(Q, inputs):
    def distance(a, b, c, d):
        if abs(a - c) % 3 == 0 and abs(b - d) % 3 == 0:
            return max(abs(a - c), abs(b - d))
        else:
            return max(abs(a - c), abs(b - d)) + 2
    
    results = []
    
    for i in range(Q):
        a, b, c, d = inputs[i]
        dist = distance(a, b, c, d)
        results.append(dist)
    
    return results

# Sample Input
Q = 2
inputs = [(4, 2, 7, 4), (9, 9, 1, 9)]
print(*fractal_distance(Q, inputs), sep='\n')