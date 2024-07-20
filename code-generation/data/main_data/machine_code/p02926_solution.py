from itertools import permutations
import math

def max_distance(N, engines):
    max_dist = 0
    for perm in permutations(engines):
        x, y = 0, 0
        for i in range(N):
            x += perm[i][0]
            y += perm[i][1]
            max_dist = max(max_dist, math.sqrt(x ** 2 + y ** 2))
    return max_dist

N = 3
engines = [(0, 10), (5, -5), (-5, -5)]
print('{:.20f}'.format(max_distance(N, engines)))