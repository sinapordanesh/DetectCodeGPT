def search(q, queries):
    M = {}
    result = []
    
    for i in range(q):
        query = queries[i].split()
        if query[0] == '0':
            M[query[1]] = int(query[2])
        elif query[0] == '1':
            result.append(M[query[1]])
    
    return result

# Sample input
q = 7
queries = ['0 blue 4', '0 red 1', '0 white 5', '1 red', '1 blue', '0 black 8', '1 black']
print(search(q, queries))