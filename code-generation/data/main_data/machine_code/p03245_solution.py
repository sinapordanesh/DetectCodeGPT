def robot_arm(N, points):
    def find_mode(x, y):
        if x > 0:
            return "R"
        elif x < 0:
            return "L"
        elif y > 0:
            return "U"
        else:
            return "D"
    
    moves = []
    for x, y in points:
        moves.append(find_mode(x, y))
    
    if len(set(moves)) != 4:
        print(-1)
        return
    
    m = 3
    d = [abs(points[i][0] - points[i-1][0]) + abs(points[i][1] - points[i-1][1]) for i in range(1, m+1)]
    
    print(m)
    print(" ".join(map(str, d)))
    for move in moves:
        print(move)

# Sample Input
N = 3
points = [(-1, 0), (0, 3), (2, -1)]
robot_arm(N, points)