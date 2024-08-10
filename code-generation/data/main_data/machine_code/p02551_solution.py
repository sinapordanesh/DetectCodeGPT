def process_queries(N, Q, queries):
    grid = [[0] * N for _ in range(N)]
    black_count = (N-2) * (N-2)
    
    for query in queries:
        q, x = query
        if q == 1:
            for j in range(1, x+1):
                if grid[0][j] == 0:
                    grid[0][j] = 1
                    black_count -= 1
        else:
            for i in range(1, x+1):
                if grid[i][0] == 0:
                    grid[i][0] = 1
                    black_count -= 1
    
    return black_count

# Sample Input 1
N = 5
Q = 5
queries = [(1, 3), (2, 3), (1, 4), (2, 2), (1, 2)]
print(process_queries(N, Q, queries))

# Sample Input 2
N = 200000
Q = 0
queries = []
print(process_queries(N, Q, queries))

# Sample Input 3
N = 176527
Q = 15
queries = [(1, 81279), (2, 22308), (2, 133061), (1, 80744), (2, 44603), 
           (1, 170938), (2, 139754), (2, 15220), (1, 172794), (1, 159290), 
           (2, 156968), (1, 56426), (2, 77429), (1, 97459), (2, 71282)]
print(process_queries(N, Q, queries))