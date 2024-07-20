def collision_time(N, airplanes):
    def get_coords(x, y, direction, seconds):
        if direction == "U":
            return (x, y + 0.1 * seconds)
        elif direction == "R":
            return (x + 0.1 * seconds, y)
        elif direction == "D":
            return (x, y - 0.1 * seconds)
        elif direction == "L":
            return (x - 0.1 * seconds, y)
        
    for i in range(N):
        x1, y1, direction1 = airplanes[i]
        for j in range(i+1, N):
            x2, y2, direction2 = airplanes[j]
            for seconds in range(1, 2001):
                x1_new, y1_new = get_coords(x1, y1, direction1, seconds)
                x2_new, y2_new = get_coords(x2, y2, direction2, seconds)
                if round(x1_new, 6) == round(x2_new, 6) and round(y1_new, 6) == round(y2_new, 6):
                    return seconds * 10
    return "SAFE"