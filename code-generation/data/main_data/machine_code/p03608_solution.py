import itertools

def shortest_distance(N, M, R, towns, roads):
    INF = float('inf')
    dist = [[INF]*N for _ in range(N)]
    
    for i in range(N):
        dist[i][i] = 0
    
    for a, b, c in roads:
        dist[a-1][b-1] = c
        dist[b-1][a-1] = c
    
    for k, i, j in itertools.permutations(towns):
        for x in range(N):
            for y in range(N):
                dist[x][y] = min(dist[x][y], dist[x][k-1]+dist[k-1][y])
    
    ans = INF
    for perm in itertools.permutations(towns):
        d = 0
        for i in range(1, R):
            d += dist[perm[i-1]-1][perm[i]-1]
        ans = min(ans, d)
    
    return ans

# Input
N, M, R = map(int, input().split())
towns = list(map(int, input().split()))
roads = [list(map(int, input().split())) for _ in range(M)]

# Calling the function
print(shortest_distance(N, M, R, towns, roads))