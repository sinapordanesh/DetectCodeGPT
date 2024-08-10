def multi_set(queries):
    from collections import Counter
    result = []
    elements_counter = Counter()
    
    for query in queries:
        operation = query[0]
        
        if operation == 0:
            x = query[1]
            elements_counter[x] += 1
            result.append(sum(elements_counter.values()))
        
        elif operation == 1:
            x = query[1]
            result.append(elements_counter[x])
        
        elif operation == 2:
            x = query[1]
            elements_counter[x] = 0
            result.append(sum(elements_counter.values()))
        
        elif operation == 3:
            L, R = query[1], query[2]
            elements_to_dump = sorted([x for x in elements_counter if L <= x <= R])
            result.extend(elements_to_dump)
    
    return result