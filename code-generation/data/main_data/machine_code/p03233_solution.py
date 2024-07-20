def min_total_weight(N, vertices):
    total_weight = 0
    min_weights = [min(vertices[i][0], vertices[i+1][1]) for i in range(N-1)]
    min_weights.append(min(vertices[N-1][0], vertices[0][1]))
    total_weight = sum(min_weights)
    
    return total_weight

# Sample Input 1
N = 3
vertices = [(1, 5), (4, 2), (6, 3)]
print(min_total_weight(N, vertices))

# Sample Input 2
N = 4
vertices = [(1, 5), (2, 6), (3, 7), (4, 8)]
print(min_total_weight(N, vertices))

# Sample Input 3
N = 6
vertices = [(19, 92), (64, 64), (78, 48), (57, 33), (73, 6), (95, 73)]
print(min_total_weight(N, vertices))