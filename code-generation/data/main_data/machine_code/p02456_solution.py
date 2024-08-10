def set_operations(q, queries):
    S = set()
    output = []
    
    for query in queries:
        operation, x = query
        
        if operation == 0:
            S.add(x)
            output.append(len(S))
        elif operation == 1:
            output.append(1 if x in S else 0)
        elif operation == 2:
            if x in S:
                S.remove(x)
    
    return output

q = 8
queries = [(0, 1), (0, 2), (0, 3), (2, 2), (1, 1), (1, 2), (1, 3), (0, 2)]

set_operations(q, queries)