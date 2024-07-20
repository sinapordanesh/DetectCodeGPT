def range_search(q, queries):
    M = {}
    output = []
    
    for query in queries:
        operation = query[0]
        
        if operation == 0: # insert
            key, x = query[1], query[2]
            M[key] = x
        elif operation == 1: # get
            key = query[1]
            output.append(M.get(key, 0))
        elif operation == 2: # delete
            key = query[1]
            if key in M:
                del M[key]
        elif operation == 3: # dump
            L, R = query[1], query[2]
            for key in sorted(M.keys()):
                if L <= key <= R:
                    output.append(f"{key} {M[key]}")
    
    return output

# Sample Input
q = 9
queries = [
    [0, 'blue', 4],
    [0, 'red', 1],
    [0, 'white', 5],
    [1, 'red'],
    [1, 'blue'],
    [2, 'red'],
    [1, 'black'],
    [1, 'red'],
    [3, 'w', 'z']
]

output = range_search(q, queries)
for o in output:
    print(o)