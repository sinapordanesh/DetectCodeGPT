def min_moves_to_beat_rooks(N, rooks):
    def distance(x1, y1, x2, y2):
        return max(abs(x1 - x2), abs(y1 - y2))
    
    distances = []
    
    for i in range(N):
        x, y = rooks[i]
        dist = 0
        for j in range(N):
            if j != i:
                dist = max(dist, distance(x, y, rooks[j][0], rooks[j][1]))
        distances.append(dist)
    
    return distances

# Sample Input 1
N = 6
rooks = [(1, 8), (6, 10), (2, 7), (4, 4), (9, 3), (5, 1)]
print(*min_moves_to_beat_rooks(N, rooks))

# Sample Input 2
N = 5
rooks = [(5, 5), (100, 100), (70, 20), (81, 70), (800, 1)]
print(*min_moves_to_beat_rooks(N, rooks))

# Sample Input 3
N = 10
rooks = [(2, 5), (4, 4), (13, 12), (12, 13), (14, 17), (17, 19), (22, 22), (16, 18), (19, 27), (25, 26)]
print(*min_moves_to_beat_rooks(N, rooks))