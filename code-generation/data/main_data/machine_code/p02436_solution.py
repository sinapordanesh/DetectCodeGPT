def queue_operations(n, queries):
    queues = [[] for _ in range(n)]
    result = []
    
    for query in queries:
        if query[0] == 0:
            queues[query[1]].append(query[2])
        elif query[0] == 1:
            if queues[query[1]]:
                result.append(queues[query[1]][0])
        elif query[0] == 2:
            if queues[query[1]]:
                queues[query[1]].pop(0)
    
    return result

# Sample input
n = 3
queries = [
    [0, 0, 1],
    [0, 0, 2],
    [0, 0, 3],
    [0, 2, 4],
    [0, 2, 5],
    [1, 0],
    [1, 2],
    [2, 0],
    [1, 0]
]

print(*queue_operations(n, queries), sep='\n')