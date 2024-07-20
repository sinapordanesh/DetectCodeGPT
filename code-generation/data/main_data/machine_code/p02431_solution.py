def dynamic_array(q, queries):
    A = []
    output = []
    
    for query in queries:
        if query[0] == 0:
            A.append(query[1])
        elif query[0] == 1:
            output.append(A[query[1]])
        elif query[0] == 2:
            A.pop()
    
    return output

# Sample input
q = 8
queries = [(0, 1), (0, 2), (0, 3), (2,), (0, 4), (1, 0), (1, 1), (1, 2)]

result = dynamic_array(q, queries)
for res in result:
    print(res)