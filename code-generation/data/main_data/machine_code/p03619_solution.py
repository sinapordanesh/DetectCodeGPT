import math

def shortest_distance(x1, y1, x2, y2, N, fountain_locations):
    def distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) * 100

    shortest_dist = distance(x1, y1, x2, y2)

    for x, y in fountain_locations:
        dist = distance(x1, y1, x, y) + distance(x, y, x2, y2)
        shortest_dist = min(shortest_dist, dist)

    return shortest_dist

# Input
x1, y1, x2, y2 = map(int, input().split())
N = int(input())
fountain_locations = []
for _ in range(N):
    X, Y = map(int, input().split())
    fountain_locations.append((X, Y))

# Output
print(shortest_distance(x1, y1, x2, y2, N, fountain_locations))