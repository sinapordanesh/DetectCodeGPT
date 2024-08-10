def priority_queue(n, queries):
    queues = [[] for _ in range(n)]
    result = []
    
    for query in queries:
        if query[0] == 0:
            queues[query[1]].append(query[2])
        elif query[0] == 1:
            if queues[query[1]]:
                result.append(max(queues[query[1]]))
        elif query[0] == 2:
            if queues[query[1]]:
                max_val = max(queues[query[1]])
                queues[query[1]].remove(max_val)
    
    return result

# Sample Input
n = 2
queries = [
    [0, 0, 3],
    [0, 0, 9],
    [0, 0, 1],
    [1, 0],
    [2, 0],
    [1, 0],
    [0, 0, 4],
    [1, 0],
    [0, 1, 8],
    [1, 1]
]

print(priority_queue(n, queries))