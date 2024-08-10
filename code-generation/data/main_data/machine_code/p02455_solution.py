def search_operations(queries):
    S = set()
    result = []
    
    for query in queries:
        operation, x = query.split()
        x = int(x)
        
        if operation == '0':
            S.add(x)
            result.append(len(S))
        elif operation == '1':
            result.append(1 if x in S else 0)
    
    return result

# Sample Input
queries = ['0 1', '0 2', '0 3', '0 2', '0 4', '1 3', '1 10']
print(search_operations(queries))