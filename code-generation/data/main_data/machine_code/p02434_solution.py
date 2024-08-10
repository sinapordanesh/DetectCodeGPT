def vector_operations(n, q, queries):
    arrays = [[] for _ in range(n)]
    result = []
    
    for query in queries:
        op, t, *args = query
        
        if op == 0:
            arrays[t].append(args[0])
        elif op == 1:
            result.append(' '.join(map(str, arrays[t])))
        elif op == 2:
            arrays[t] = []
    
    return result

# Sample Input
n = 3
q = 13
queries = [
    [0, 0, 1],
    [0, 0, 2],
    [0, 0, 3],
    [0, 1, -1],
    [0, 2, 4],
    [0, 2, 5],
    [1, 0],
    [1, 1],
    [1, 2],
    [2, 1],
    [1, 0],
    [1, 1],
    [1, 2]
]

# Sample Output
print(*vector_operations(n, q, queries), sep='\n')