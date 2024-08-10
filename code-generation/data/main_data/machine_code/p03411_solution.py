def maximum_friendly_pairs(N, red_points, blue_points):
    pairs = 0
    red_points.sort()
    blue_points.sort()
    
    for r, b in zip(red_points, blue_points):
        if r[0] < b[0] and r[1] < b[1]:
            pairs += 1
    
    return pairs

# Sample Input 1
N = 3
red_points = [(2, 0), (3, 1), (1, 3)]
blue_points = [(4, 2), (0, 4), (5, 5)]
print(maximum_friendly_pairs(N, red_points, blue_points))

# Sample Input 2
N = 3
red_points = [(0, 0), (1, 1), (5, 2)]
blue_points = [(2, 3), (3, 4), (4, 5)]
print(maximum_friendly_pairs(N, red_points, blue_points))

# Sample Input 3
N = 2
red_points = [(2, 2), (3, 3)]
blue_points = [(0, 0), (1, 1)]
print(maximum_friendly_pairs(N, red_points, blue_points))

# Sample Input 4
N = 5
red_points = [(0, 0), (7, 3), (2, 2), (4, 8), (1, 6)]
blue_points = [(8, 5), (6, 9), (5, 4), (9, 1), (3, 7)]
print(maximum_friendly_pairs(N, red_points, blue_points))

# Sample Input 5
N = 5
red_points = [(0, 0), (1, 1), (5, 5), (6, 6), (7, 7)]
blue_points = [(2, 2), (3, 3), (4, 4), (8, 8), (9, 9)]
print(maximum_friendly_pairs(N, red_points, blue_points))