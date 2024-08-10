from itertools import combinations

def shortest_distance_sum(H, W, N, white_squares):
    MOD = 10**9 + 7
    white_squares_set = set(white_squares)
    
    def bfs_distance(start, end):
        queue = [(start[0], start[1], 0)]
        visited = set()
        while queue:
            x, y, dist = queue.pop(0)
            if (x, y) == end:
                return dist
            visited.add((x, y))
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < H and 0 <= new_y < W and (new_x, new_y) not in white_squares_set and (new_x, new_y) not in visited:
                    queue.append((new_x, new_y, dist + 1))
        return -1

    total_distance = 0
    for pair in combinations(white_squares, 2):
        dist = bfs_distance(pair[0], pair[1])
        total_distance += dist
    
    return total_distance % MOD

# Input
H, W = map(int, input().split())
N = int(input())
white_squares = [tuple(map(int, input().split())) for _ in range(N)]

# Output
print(shortest_distance_sum(H, W, N, white_squares))