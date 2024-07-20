def min_max_colors(N, ratings):
    colors = [0] * 9
    for rating in ratings:
        if rating < 400:
            colors[0] = 1
        elif rating < 800:
            colors[1] = 1
        elif rating < 1200:
            colors[2] = 1
        elif rating < 1600:
            colors[3] = 1
        elif rating < 2000:
            colors[4] = 1
        elif rating < 2400:
            colors[5] = 1
        elif rating < 2800:
            colors[6] = 1
        elif rating < 3200:
            colors[7] = 1
        else:
            colors[8] += 1
    
    min_colors = sum(colors[:8]) + (1 if colors[8] > 0 else 0)
    max_colors = sum(colors[:8]) + colors[8]
    
    return min_colors, max_colors