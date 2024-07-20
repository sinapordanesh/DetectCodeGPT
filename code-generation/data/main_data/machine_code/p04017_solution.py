def minimum_days(N, hotels, L, Q, queries):
    distances = [hotels[i] - hotels[i-1] for i in range(1, N)]
    
    def calculate_days(start, end):
        total_days = 1
        current_distance = 0
        for i in range(start, end):
            current_distance += distances[i]
            if current_distance > L:
                total_days += 1
                current_distance = distances[i]
        return total_days
    
    result = []
    for query in queries:
        result.append(calculate_days(query[0]-1, query[1]-1))
    
    return result

# Sample Input
N = 9
hotels = [1, 3, 6, 13, 15, 18, 19, 29, 31]
L = 10
Q = 4
queries = [(1, 8), (7, 3), (6, 7), (8, 5)]

print(*minimum_days(N, hotels, L, Q, queries), sep='\n')