def pairs_with_integer_distance(N, D, points):
    def distance(p1, p2):
        return sum([(p1[i] - p2[i]) ** 2 for i in range(D)]) ** 0.5
    
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            dist = distance(points[i], points[j])
            if dist.is_integer():
                count += 1
    return count

# Sample Input 1
print(pairs_with_integer_distance(3, 2, [[1, 2], [5, 5], [-2, 8]]))

# Sample Input 2
print(pairs_with_integer_distance(3, 4, [[-3, 7, 8, 2], [-12, 1, 10, 2], [-2, 8, 9, 3]]))

# Sample Input 3
print(pairs_with_integer_distance(5, 1, [[1], [2], [3], [4], [5]]))