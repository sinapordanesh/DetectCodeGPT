def robot_arm(N, points):
    def get_mode(x1, y1, x2, y2):
        if x2 > x1:
            return "R"
        elif x2 < x1:
            return "L"
        elif y2 > y1:
            return "U"
        else:
            return "D"
    
    x = [0] + [point[0] for point in points]
    y = [0] + [point[1] for point in points]
    
    for m in range(1, 41):
        for d_combination in product(range(1, 10**12 + 1), repeat=m):
            modes = [get_mode(x[i], y[i], x[i+1], y[i+1]) for i in range(N)]
            if all([sum([d_combination[i] if modes[i] == "R" else -d_combination[i] if modes[i] == "L" else 0 for i in range(j)]) == x[j] and sum([d_combination[i] if modes[i] == "U" else -d_combination[i] if modes[i] == "D" else 0 for i in range(j)]) == y[j] for j in range(1, N+1)]):
                return (m, d_combination, modes)
    
    return -1