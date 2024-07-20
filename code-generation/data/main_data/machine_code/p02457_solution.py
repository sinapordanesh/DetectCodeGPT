def range_search(q, queries):
    S = set()
    output = []
    
    for query in queries:
        operation = query[0]
        
        if operation == 0:
            x = query[1]
            S.add(x)
            output.append(len(S))
        elif operation == 1:
            x = query[1]
            output.append(1 if x in S else 0)
        elif operation == 2:
            x = query[1]
            S.discard(x)
        elif operation == 3:
            L = query[1]
            R = query[2]
            dump_elements = sorted([x for x in S if L <= x <= R])
            for element in dump_elements:
                output.append(element)
    
    return output

# Sample Input
q = 9
queries = [(0, 1), (0, 2), (0, 3), (2, 2), (1, 1), (1, 2), (1, 3), (0, 4), (3, 2, 4)]

output = range_search(q, queries)
for o in output:
    print(o)