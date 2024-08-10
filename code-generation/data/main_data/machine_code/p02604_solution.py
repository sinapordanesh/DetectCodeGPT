def min_walking_distances(N, areas):
    def manhattan_distance(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    total_pop = sum(pop for x, y, pop in areas)
    
    ans = []
    for k in range(N+1):
        dist = [[float('inf')] * N for _ in range(1 << N)]
        dist[0] = [0] * N
        for S in range(1 << N):
            for i in range(N):
                if not S & 1 << i:
                    continue
                for j in range(N):
                    if S & 1 << j:
                        continue
                    dist[S | 1 << j][j] = min(dist[S | 1 << j][j], dist[S][i] + manhattan_distance(*areas[i][:2], *areas[j][:2]) * areas[j][2])
        ans.append(sum(dist[-1]))
    
    return ans

# Sample Input
N = 3
areas = [(1, 2, 300), (3, 3, 600), (1, 4, 800)]
print(*min_walking_distances(N, areas))