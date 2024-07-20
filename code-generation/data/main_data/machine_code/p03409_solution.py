def max_friendly_pairs(N, red_points, blue_points):
    pairs = 0
    red_points.sort(key=lambda x: (x[0], x[1]))
    blue_points.sort(key=lambda x: (x[0], x[1]))
    
    for r in red_points:
        for b in blue_points:
            if r[0] < b[0] and r[1] < b[1]:
                pairs += 1
                blue_points.remove(b)
                break
                
    return pairs