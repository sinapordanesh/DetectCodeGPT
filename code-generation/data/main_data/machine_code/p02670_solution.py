def number_of_pairs(N, seats):
    cinema = [[0 for _ in range(N)] for _ in range(N)]
    viewers = {}
    for i in range(N):
        for j in range(N):
            viewers[seats[i*N + j]] = (i, j)
    
    def bfs(x, y):
        queue = [(x, y)]
        visited = [[False for _ in range(N)] for _ in range(N)]
        while queue:
            i, j = queue.pop(0)
            visited[i][j] = True
            if cinema[i][j] == seats[x]:
                return abs(viewers[seats[x]][0] - i) + abs(viewers[seats[x]][1] - j)
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_i, new_j = i + dx, j + dy
                if 0 <= new_i < N and 0 <= new_j < N and not visited[new_i][new_j]:
                    queue.append((new_i, new_j))
    
    pairs = 0
    for i in range(1, N*N + 1):
        x, y = viewers[i]
        distances = []
        for j in range(i+1, N*N + 1):
            distances.append(bfs(j, i))
        min_distance = min(distances)
        pairs += distances.count(min_distance)
    
    return pairs

N = 3
seats = [1, 3, 7, 9, 5, 4, 8, 6, 2]
print(number_of_pairs(N, seats))

N = 4
seats = [6, 7, 1, 4, 13, 16, 10, 9, 5, 11, 12, 14, 15, 2, 3, 8]
print(number_of_pairs(N, seats))

N = 6
seats = [11, 21, 35, 22, 7, 36, 27, 34, 8, 20, 15, 13, 16, 1, 24, 3, 2, 17, 26, 9, 18, 32, 31, 23, 19, 14, 4, 25, 10, 29, 28, 33, 12, 6, 5, 30]
print(number_of_pairs(N, seats))