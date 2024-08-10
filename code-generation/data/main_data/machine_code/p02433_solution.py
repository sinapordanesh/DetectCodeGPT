def dynamic_list(q, queries):
    L = []
    cursor = 0
    
    for query in queries:
        operation = query[0]
        
        if operation == 0:
            x = query[1]
            L.insert(cursor, x)
            cursor += 1
        elif operation == 1:
            d = query[1]
            if d > 0:
                cursor = len(L)
            elif d < 0:
                cursor = 0
        else:
            del L[cursor]
            if cursor == len(L):
                cursor = len(L) - 1
    
    return L

# Sample Input
q = 5
queries = [(0, 1), (0, 2), (0, 3), (1, 1), (2, 0)]
dynamic_list(q, queries)