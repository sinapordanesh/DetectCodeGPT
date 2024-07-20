def calender_colors(N, M, colors):
    from itertools import combinations

    def distance(color1, color2):
        return (color1[0] - color2[0])**2 + (color1[1] - color2[1])**2 + (color1[2] - color2[2])**2

    max_distance = 0
    for subset in combinations(colors, M):
        total_distance = 0
        for color1 in subset:
            for color2 in subset:
                total_distance += distance(color1, color2)
        max_distance = max(max_distance, total_distance)

    return max_distance

# Sample Input 1
N = 3
M = 2
colors = [(0, 0, 0), (10, 10, 10), (100, 100, 100)]
print(calender_colors(N, M, colors))

# Sample Input 2
N = 5
M = 3
colors = [(12.0, 15.0, 9.0), (10.0, -3.0, 2.2), (3.5, 6.8, 9.0), (2.1, 4.4, 5.9), (1.2, 4.0, -5.4)]
print(calender_colors(N, M, colors))

# Sample Input 3
N = 2
M = 1
colors = [(1.0, 1.0, 1.0), (0.0, 0.0, 0.0)]
print(calender_colors(N, M, colors))