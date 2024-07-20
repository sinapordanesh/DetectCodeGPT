def find_distance(N, Q, roadworks, people):
    def check_blocked(x, t):
        for i in range(N):
            if roadworks[i][0] <= x < roadworks[i][1]:
                if roadworks[i][2] <= t < roadworks[i][3]:
                    return roadworks[i][1]
        return -1

    result = []
    for i in range(Q):
        d = people[i]
        distance = 0
        while True:
            blocked_point = check_blocked(distance, d + distance)
            if blocked_point == -1:
                distance += 1
            else:
                result.append(blocked_point)
                break
        if distance > 10**9:
            result.append(-1)
    
    return result

# Sample Input
N = 4
Q = 6
roadworks = [(1, 3, 2, 2.5), (7, 13, 10, 12.5), (18, 20, 13, 19.5), (3, 4, 2, 3.5)]
people = [0, 1, 2, 3, 5, 8]

output = find_distance(N, Q, roadworks, people)
for distance in output:
    print(distance)