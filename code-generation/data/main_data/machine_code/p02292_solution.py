def direction(p0, p1, p2):
    def cross_product(p0, p1, p2):
        return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p1[1] - p0[1]) * (p2[0] - p0[0])
    
    if cross_product(p0, p1, p2) > 0:
        return "COUNTER_CLOCKWISE"
    elif cross_product(p0, p1, p2) < 0:
        return "CLOCKWISE"
    else:
        if p2[0] > min(p0[0], p1[0]) and p2[0] < max(p0[0], p1[0]) and p2[1] > min(p0[1], p1[1]) and p2[1] < max(p0[1], p1[1]):
            return "ON_SEGMENT"
        elif p2[0] < min(p0[0], p1[0]) or p2[0] > max(p0[0], p1[0]) or p2[1] < min(p0[1], p1[1]) or p2[1] > max(p0[1], p1[1]):
            return "ONLINE_FRONT"
        else:
            return "ONLINE_BACK"