def most_powerful_spell(datasets):
    results = []
    for data in datasets:
        n, a, s, g = data[0]
        arrows = data[1:]
        
        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        
        for arrow in arrows:
            x, y, lab = arrow
            adj_list[x].append((y, lab))
        
        visited = [False] * n
        path = []
        
        def dfs(node):
            visited[node] = True
            for neighbor, lab in adj_list[node]:
                if not visited[neighbor]:
                    path.append(lab)
                    if neighbor == g:
                        return True
                    if dfs(neighbor):
                        return True
                    path.pop()
            return False
        
        if dfs(s):
            results.append("".join(path))
        else:
            results.append("NO")
    
    return results

# Sample Input
datasets = [
    [
        (4, 7, 0, 2),
        (0, 1, "abra"),
        (0, 1, "oil"),
        (2, 0, "ket"),
        (1, 3, "cada"),
        (3, 3, "da"),
        (3, 2, "bra"),
        (2, 3, "ket")
    ],
    [
        (2, 2, 0, 1),
        (0, 0, "a"),
        (0, 1, "b")
    ],
    [
        (5, 6, 3, 0),
        (3, 1, "op"),
        (3, 2, "op"),
        (3, 4, "opq"),
        (1, 0, "st"),
        (2, 0, "qr"),
        (4, 0, "r")
    ],
    [
        (2, 1, 0, 1),
        (1, 1, "loooop")
    ],
    [
        (0, 0, 0, 0)
    ]
]

results = most_powerful_spell(datasets)
for result in results:
    print(result)