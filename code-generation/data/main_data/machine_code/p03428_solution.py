def probability_of_falling(N, points):
    R = 10 ** 10 ** 10
    probs = []
    
    for i in range(N):
        x_i, y_i = points[i]
        dist = (x_i ** 2 + y_i ** 2) ** 0.5
        prob = 0
        if dist <= R:
            prob = 1 / (N + 1)
        probs.append(prob)
    
    return probs