def closed_curve(N, sequence):
    
    def construct_closed_curve(N, sequence):
        curve = []
        x = 0
        y = 0.5
        for i in range(2**N):
            curve.append((x, y))
            if sequence[i] == 0:
                y = 1 - y
            x += 1
        return curve
    
    curve = construct_closed_curve(N, sequence)
    
    for i in range(2**N):
        S = set()
        for j in range(N):
            if i & (1 << j):
                S.add(j)
        B_S = set([(i+0.5, 0.5) for i in S])
        valid = True
        for point in curve:
            if point in B_S:
                valid = False
                break
        if valid:
            return "Possible\n" + str(len(curve)) + "\n" + "\n".join([str(point[0]) + " " + str(point[1]) for point in curve])
    
    return "Impossible"