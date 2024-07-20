def range_add_query(n, q, queries):
    A = [0] * n
    result = []
    
    for query in queries:
        if query[0] == 0:
            s, t, x = query[1], query[2], query[3]
            for i in range(s-1, t):
                A[i] += x
        elif query[0] == 1:
            result.append(A[query[1]-1])
    
    return result

# Sample Input 1
n1 = 3
q1 = 5
queries1 = [(0, 1, 2, 1), (0, 2, 3, 2), (0, 3, 3, 3), (1, 2), (1, 3)]
print(range_add_query(n1, q1, queries1))

# Sample Input 2
n2 = 4
q2 = 3
queries2 = [(1, 2), (0, 1, 4, 1), (1, 2)]
print(range_add_query(n2, q2, queries2))