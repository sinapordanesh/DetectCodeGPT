import math

def average_length_of_paths():
    N = int(input())
    towns = []
    for _ in range(N):
        x, y = map(int, input().split())
        towns.append((x, y))
    
    total_distance = 0
    permutations = itertools.permutations(towns)
    total_permutations = math.factorial(N)
    
    for path in permutations:
        distance = 0
        for i in range(N-1):
            distance += math.sqrt((path[i][0] - path[i+1][0])**2 + (path[i][1] - path[i+1][1])**2)
        total_distance += distance
    
    avg_length = total_distance / total_permutations
    print(avg_length)

average_length_of_paths()