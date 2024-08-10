def count_holes(datasets):
    for data in datasets:
        n, m, t, p, *instructions = data
        paper = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(t):
            d, c = instructions[i*2], instructions[i*2+1]
            if d == 1:
                for j in range(c, n):
                    for k in range(m):
                        paper[k][j] = 0
                n = c
            else:
                for j in range(c, m):
                    for k in range(n):
                        paper[j][k] = 0
                m = c
        
        for i in range(p):
            x, y = instructions[t*2+i*2], instructions[t*2+i*2+1]
            print(paper[y][x]) 

datasets = [
    [2, 1, 1, 1, 1, 1, 0, 0],
    [1, 3, 2, 1, 2, 1, 2, 1, 0, 0],
    [10, 8, 3, 2, 2, 2, 1, 3, 1, 1, 0, 1, 3, 4, 3, 3, 3, 2, 1, 2, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0]
]

count_holes(datasets)