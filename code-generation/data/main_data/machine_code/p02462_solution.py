def multi_map(queries):
    M = {}
    result = []
    
    for query in queries:
        operation = query[0]
        
        if operation == 0:
            key = query[1]
            value = query[2]
            if key not in M:
                M[key] = []
            M[key].append(value)
        
        elif operation == 1:
            key = query[1]
            if key in M:
                result.extend(M[key])
        
        elif operation == 2:
            key = query[1]
            if key in M:
                del M[key]
        
        elif operation == 3:
            L = query[1]
            R = query[2]
            for key in sorted(M.keys()):
                if L <= key <= R:
                    for value in M[key]:
                        result.append((key, value))
    
    for r in result:
        if type(r) == tuple:
            print(r[1])
        else:
            print(r)