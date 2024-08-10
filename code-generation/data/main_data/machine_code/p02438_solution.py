def splice(n, q, queries):
    lists = [[] for _ in range(n)]
    output = []
    
    for query in queries:
        if query[0] == 0:  # insert
            t, x = query[1:]
            lists[t].append(x)
        elif query[0] == 1:  # dump
            t = query[1]
            output.append(" ".join(map(str, lists[t])))
        elif query[0] == 2:  # splice
            s, t = query[1:]
            lists[t] += lists[s]
            lists[s] = []
    
    return output

# Sample input
n = 3
q = 10
queries = [
    (0, 0, 1),
    (0, 0, 2),
    (0, 0, 3),
    (0, 1, 4),
    (0, 1, 5),
    (2, 1, 0),
    (0, 2, 6),
    (1, 0),
    (1, 1),
    (1, 2)
]

print(splice(n, q, queries))