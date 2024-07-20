def total_distance(N, segments):
    segments.sort(key=lambda x: x[1])
    total = 0
    for i in range(N):
        if i % 2 == 0:
            total += segments[i][1]
        else:
            total -= segments[i][0]
    return total

# Sample Input 1
N = 3
segments = [[-5, 1], [3, 7], [-4, -2]]
print(total_distance(N, segments))

# Sample Input 2
N = 3
segments = [[1, 2], [3, 4], [5, 6]]
print(total_distance(N, segments))

# Sample Input 3
N = 5
segments = [[-2, 0], [-2, 0], [7, 8], [9, 10], [-2, -1]]
print(total_distance(N, segments))