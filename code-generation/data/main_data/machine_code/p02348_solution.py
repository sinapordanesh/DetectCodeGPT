def range_update_query(n, queries):
    A = [2**31-1] * n
    
    def update(s, t, x):
        for i in range(s, t+1):
            A[i] = x
    
    def find(i):
        return A[i]
    
    output = []
    for query in queries:
        if query[0] == 0:
            update(query[1], query[2], query[3])
        elif query[0] == 1:
            output.append(find(query[1]))
    
    return output

# Sample Input 1
n = 3
queries = [(0, 0, 1, 1), (0, 1, 2, 3), (0, 2, 2, 2), (1, 0), (1, 1)]
print(range_update_query(n, queries))

# Sample Input 2
n = 1
queries = [(1, 0), (0, 0, 0, 5), (1, 0)]
print(range_update_query(n, queries))