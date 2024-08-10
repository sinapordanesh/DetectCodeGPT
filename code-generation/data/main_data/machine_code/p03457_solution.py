def atcoder_trip(N, points):
    x_curr, y_curr, t_curr = 0, 0, 0
    
    for i in range(N):
        t_next, x_next, y_next = points[i]
        dist = abs(x_next - x_curr) + abs(y_next - y_curr)
        time_diff = t_next - t_curr
        
        if (time_diff < dist) or ((time_diff - dist) % 2 != 0):
            return "No"
        
        x_curr, y_curr, t_curr = x_next, y_next, t_next
    
    return "Yes"