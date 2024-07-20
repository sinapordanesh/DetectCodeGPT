import itertools

def sum_of_scores(N, points):
    MOD = 998244353
    total_score = 0
    
    for i in range(1, 2**N):
        current_points = []
        for j in range(N):
            if i & (1 << j):
                current_points.append(points[j])
        
        if len(current_points) < 3:
            continue
        
        x_values = [point[0] for point in current_points]
        y_values = [point[1] for point in current_points]
        
        total = 0
        for a, b, c in itertools.combinations(range(len(current_points)), 3):
            count = 0
            for j in range(len(current_points)):
                if j == a or j == b or j == c:
                    continue
                if (x_values[b] - x_values[a]) * (y_values[j] - y_values[a]) == (x_values[j] - x_values[a]) * (y_values[b] - y_values[a]):
                    count += 1
            if count == 0:
                total += 1
        
        total_score += pow(2, total - len(current_points), MOD)
    
    return total_score % MOD

# Sample Input 1
N = 4
points = [(0, 0), (0, 1), (1, 0), (1, 1)]
print(sum_of_scores(N, points))

# Sample Input 2
N = 5
points = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1)]
print(sum_of_scores(N, points))

# Sample Input 3
N = 1
points = [(3141, 2718)]
print(sum_of_scores(N, points))