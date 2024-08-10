import math

def min_exposure_time(x_s, y_s, x_t, y_t, N, barriers):
    
    def distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def is_inside_barrier(x, y, barrier):
        return distance(x, y, barrier[0], barrier[1]) <= barrier[2]
    
    def is_exposed(x, y, barriers):
        for barrier in barriers:
            if is_inside_barrier(x, y, barrier):
                return False
        return True
    
    def dfs(x, y, time):
        if (x, y) == (x_t, y_t):
            return time
        min_time = float('inf')
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                new_x, new_y = x + dx, y + dy
                if is_exposed(new_x, new_y, barriers):
                    new_time = time + distance(x, y, new_x, new_y)
                    new_barriers = [(bx, by, br) for bx, by, br in barriers if not is_inside_barrier(new_x, new_y, (bx, by, br))]
                    min_time = min(min_time, dfs(new_x, new_y, new_time, new_barriers))
        return min_time
    
    return dfs(x_s, y_s, 0, barriers)