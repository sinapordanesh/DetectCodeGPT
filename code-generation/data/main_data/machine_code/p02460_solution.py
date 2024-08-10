def delete_map(q, queries):
    M = {}
    result = []
    
    for i in range(q):
        query = queries[i]
        operation = int(query[0])
        key = query[1]
        
        if operation == 0:
            x = int(query[2])
            M[key] = x
        elif operation == 1:
            if key in M:
                result.append(M[key])
            else:
                result.append(0)
        elif operation == 2:
            del M[key]
    
    for r in result:
        print(r)

# Sample Input
q = 8
queries = [
    [0, "blue", 4],
    [0, "red", 1],
    [0, "white", 5],
    [1, "red"],
    [1, "blue"],
    [2, "red"],
    [1, "black"],
    [1, "red"]
]

delete_map(q, queries)