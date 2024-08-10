def stack_operations(n, queries):
    stacks = [[] for _ in range(n)]
    output = []
    
    for query in queries:
        if query[0] == 0:
            t, x = query[1], query[2]
            stacks[t].append(x)
        elif query[0] == 1:
            t = query[1]
            if stacks[t]:
                output.append(stacks[t][-1])
        elif query[0] == 2:
            t = query[1]
            if stacks[t]:
                stacks[t].pop()
    
    return output

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

output = stack_operations(n, queries)
for item in output:
    print(item)