def RMQ_RAQ(n, q, queries):
    A = [0] * n
    result = []
    
    for query in queries:
        if query[0] == 0:
            s, t, x = query[1], query[2], query[3]
            for i in range(s, t+1):
                A[i] += x
        elif query[0] == 1:
            s, t = query[1], query[2]
            result.append(min(A[s:t+1]))
    
    return result

# Sample Input
n = 6
q = 7
queries = [
    [0, 1, 3, 1],
    [0, 2, 4, -2],
    [1, 0, 5],
    [1, 0, 1],
    [0, 3, 5, 3],
    [1, 3, 4],
    [1, 0, 5]
]

# Sample Output
print(RMQ_RAQ(n, q, queries))