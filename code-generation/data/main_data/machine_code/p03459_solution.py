def can_carry_out_plan(N, points):
    x = 0
    y = 0
    t = 0
    
    for i in range(N):
        t_diff = points[i][0] - t
        dist = abs(points[i][1] - x) + abs(points[i][2] - y)
        
        if t_diff < dist or (t_diff % 2 != dist % 2):
            return "No"
        
        x = points[i][1]
        y = points[i][2]
        t = points[i][0]
    
    return "Yes"