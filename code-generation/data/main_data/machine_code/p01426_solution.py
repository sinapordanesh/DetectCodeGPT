def vector_compression(N, M, vectors):
    def squared_length(v):
        return sum([x*x for x in v])
    
    result = 0
    for i in range(M):
        min_length = float('inf')
        for j in range(i):
            diff = [vectors[i][k] - vectors[j][k] for k in range(N)]
            min_length = min(min_length, squared_length(diff))
        result += min_length
    
    return result

# Sample Input 1
print(vector_compression(2, 3, [[1.0, 1.0], [-1.0, 0.0], [0.5, 0.5]]))

# Sample Input 2
print(vector_compression(1, 1, [[1.0]]))

# Sample Input 3
print(vector_compression(4, 3, [[1.0, 1.0, 0.0, 0.0], [-1.0, 0.0, -1.0, 0.0], [0.5, 0.5, 0.5, 0.5]]))